class MNIST_v4(torch.nn.Module):

    training_losses     = []    #for plotting purposes
    validation_losses   = []    #for plotting purposes
    training_accuracy   = []    #for plotting purposes
    validation_accuracy = []    #for plotting purposes
    criterion = None            #for criterion check
    optim     = None            #for optim check
    nonlinear = False           #as a switch between linear and nonlinear outputs

    def __init__(self,
                 in_features,
                 out_features,
                 layers=None,
                 optim=None,
                 criterion=None,
                 dropout=0.2):

        super().__init__()

        if optim is not None:
            set_optim(optim)
        if criterion is not None:
            set_criterion(criterion)

        # define the architecture if layers argument provided
        if layers:
            assert isinstance(layers,list) or isinstance(layers, tuple), \
                                        "layers argument must be list or tuple"
        layerlist = []

        for neurons_in_layer in layers:
            layerlist.append(torch.nn.Linear(in_features,neurons_in_layer))
            layerlist.append(torch.nn.ReLU(inplace=True))
            #layerlist.append(torch.nn.BatchNorm1d(i))
            layerlist.append(torch.nn.Dropout(dropout))
            in_features = neurons_in_layer
        layerlist.append(torch.nn.Linear(layers[-1],out_features))

        # the final architecture
        self.layers = torch.nn.Sequential(*layerlist)


    def set_optim(self, optim, lr):

        '''Sets optimiser. Must be called separately'''

        self.optim = optim(self.parameters(), lr=lr)

    def set_criterion(self, criterion):

        '''Sets the loss function. Must be called separately'''

        self.criterion = criterion

    def get_accuracy(self, preds, labels):

        '''
        Calculated accuracy using torch.max by comparing the predicted
        and the final labels, and taking its mean.
        '''

        value, predicted_class = torch.max(preds, dim=1)
        return (predicted_class == labels).float().mean()*100

    def is_problem_linear(self, check=True, activation=None):

        '''
        Currently buggy. Needs further testing.
        Used to tranform the architecture from a linear to a nonlinear model.
        This function is used in the self.forward function.
        '''

        if not check and not activation:
            raise ValueError("Activation function undefined for nonlinear problem")
        if check:
            self.nonlinear = True #used as a switch in forward
            self.final_activation = activation


    def _get_mean_(self, listOfTensors):

        '''
        Used to first converst the list of tensors into tensors, and then
        take its mean.
        '''

        return torch.stack(listOfTensors).mean()

    def forward(self, images):

        '''
        This function matrix multiplies inputs with weights and biases and
        returns linear or non-linear outputs.
        '''

        images = images.view(-1,28*28)
        preds = self.layers(images)
        if self.nonlinear:
            return self.final_activation(preds, dim=-1)
        return preds

    def calculate_loss(self, preds, labels):
        if self.criterion is None:
            raise ValueError("Loss Function not set. Call set_criterion to set a loss function")
        return self.criterion(preds, labels)

    def learn_weights(self, preds, labels):

        '''
        Only to be used internally in the class, this function calculates
        the loss, gradients and accordingly updates the weights.
        Loss is returned for printing purposes.
        '''

        loss = self.calculate_loss(preds, labels)
        loss.backward()
        if self.optim is None:
            raise ValueError("Optimizer not set. Call set_optim to set an optimizer function")
        self.optim.step()
        self.optim.zero_grad()
        return loss

    def train(self,
              epochs,
              train_loader,
              validation_loader=None,
              verbose=True):

        '''
        The main workhorse function that trains the model weights and biases.
        '''

        for epoch in range(epochs):

            for batch_no, (images, labels) in enumerate(train_loader):
                preds = self.forward(images)
                loss = self.learn_weights(preds, labels)

            # gets training accuracy and loss for the whole epoch
            train_accuracy = self.get_accuracy(preds, labels).mean()
            # already a tensor hence not used _get_mean_
            self.training_accuracy.append(train_accuracy)
            # append training (last loss) loss
            self.training_losses.append(loss)

            # if printing is opted for while training.
            if verbose:
                print(f"epoch no: [{epoch+1}] ===> loss :: {loss:4f} and " \
                      f"accuracy :: {train_accuracy}")

            # executed only if the validation set is passed
            if validation_loader:
                mean_loss, mean_accuracy = self.check_model_sanity(validation_loader)
                print(f"epoch no [{epoch+1}] ======> mean_loss_val = {mean_loss:4f}," \
                      f" mean_accuracy_val = {mean_accuracy:4f}")


    def check_model_sanity(self, data_loader):

        '''
        Contains the logic for running accuracy and loss on the validation set,
        and the test set.
        '''

        validation_accuracy = []

        with torch.no_grad():

            # get a list of predictions, labels, losses of the validation set
            val_preds  = [self.forward(images) for images, _ in data_loader]

            val_labels =              [ labels for _, labels in data_loader]

            val_losses = [self.calculate_loss(pred, labels)
                          for pred, labels in zip(val_preds, val_labels)]

            # mean validation loss
            val_mean_loss = self._get_mean_(val_losses)

            # used for plotting
            self.validation_losses.append(val_mean_loss)

            # calculation of validation accuracy
            val_accuracy = [self.get_accuracy(pred, label)
                            for pred, label in zip(val_preds, val_labels)]

            # mean validation accuracy
            val_mean_accuracy = self._get_mean_(val_accuracy)

            # for plotting purposes
            self.validation_accuracy.append(val_mean_accuracy)

            return val_mean_loss, val_mean_accuracy #returns test/val mean metrics

    def predict(self, dataloader_object):

        '''
        User interface for making predictions on the test set.
        '''

        mean_loss, mean_accuracy = self.check_model_sanity()
        print(f"mean_loss_val = {mean_loss:4f}, mean_accuracy_val = {mean_accuracy:4f}")

    def plot_losses(self, train=False):
        if not train and not self.validation_accuracy:
            return "Validation loss"
        if not train:
            self._plot(self.validation_losses)
        else: self._plot(self.training_losses)

    def plot_accuracies(self, train=False):
        if not train and not self.validation_accuracy:
            return "Validation losses not computed"
        if not train:
            self._plot(self.validation_accuracy)
        else: self._plot(self.training_accuracy)

    def _plot(self,x):
        plt.plot(x, '-x')
        plt.xlabel('epoch')
        plt.ylabel('accuracy')
        plt.title('Accuracy vs. No. of epochs');
