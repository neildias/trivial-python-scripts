import numpy as np
import pandas as pd

from sklearn import model_selection
from sklearn import preprocessing
from sklearn import linear_model
from sklearn import tree
from sklearn import feature_extraction
from sklearn import feature_selection
from sklearn import datasets
from sklearn import cluster
from sklearn import clone
from sklearn import ensemble
from sklearn import kernel_approximation, kernel_ridge
from sklearn import metrics
from sklearn import manifold
from sklearn import svm
from sklearn import naive_bayes, neighbors
from sklearn import neural_network
from sklearn import pipeline
from sklearn import semi_supervised
from sklearn import decomposition, discriminant_analysis
from sklearn import clone
from sklearn import utils

class Base(object):
    X_tr = Xt = y_tr = yt = dataset = original_data = None
    null_present = None
    numericalised = None
    model_objects = dict()
    results = dict()

    def __init__(self, dataset):
        self.dataset = self.original_data = dataset.copy()

    def data(self, dataset):
        self.dataset = self.original_data = dataset.copy()
        return self

    def null_check(self):
        if self.dataset is None:
            print("No dataset found")
            return
        check = True if self.dataset.isnull().mean().sum() <= 0 else False
        if check:
            self.null_present = False
            print("No null values found")
        else:
            self.null_present = True
            print("Null values present")
        return self

    def clean(self, by_mean=True):
        if self.dataset is None:
            print("Not data available to clean")
            return self
        for col in self.dataset.columns:
            if self.dataset[col].dtypes == "object":
                self.dataset[col] = self.dataset[col].fillna(self.dataset[col].mode()[0])
            else:
                if not by_mean:
                    self.dataset[col] = self.dataset[col].fillna(self.dataset[col].median())
                else:
                    self.dataset[col] = self.dataset[col].fillna(self.dataset[col].mean())
        print("Cleaning completed. Call null_check to verify...")
        self.null_present = False
        return self

    def clean_by_median(self):
        if self.dataset is None:
            print("No dataset found")
            return
        self.clean(by_mean=False)
        return self

    def show(self):
        if self.dataset is None:
            print("No dataset found")
            return
        print(self.dataset)
        return self

    def isnumerical(self):
        if self.dataset is None:
            print("No dataset found")
            return self
        if self.dataset.select_dtypes(include='object').empty:
            self.numericalised = True
            print("No object datatypes found")
        else:
            self.numericalised = False
            print("Warning! Object datatypes found...")
        return self

    def numericalise(self):
        if self.dataset is None:
            print("No dataset found")
            return self
        for col in self.dataset.select_dtypes(include="object").columns:
            self.dataset[col] = self.dataset[col].astype("category").cat.codes
        self.numericalised = True
        return self

    def reset_data(self):
        if self.dataset is None:
            print("No dataset found")
            return self
        self.dataset = self.original_data
        return self

    def data_ismodel_ready(self):
        if self.dataset is None:
            print("No dataset found")
            return self
        if self.numericalised is None: self.isnumerical()
        if self.null_present is None: self.null_check()
        if self.numericalised and not self.null_present:
            print("Data is model ready. Proceed to validation splits and modelling.")
        else:
            print("Data is not model ready")
        return self

    def make_model_ready(self):
        self.clean()
        self.numericalise()
        self.data_ismodel_ready()
        return self

    def train_test_split(self, label):
        features = self.dataset.drop([label], axis=1).copy().values
        target = self.dataset[label].copy().values

        self.X_tr, self.Xt, self.y_tr, self.yt = model_selection.train_test_split(features, target)
        print(self.X_tr.shape, self.Xt.shape)
        return self


@pd.api.extensions.register_dataframe_accessor("Linear_Regression")
class LinearRegression(Base):

    def __init__(self, dataframe, verbose=False):
        super().__init__(dataframe)
        if verbose: self.printer()

    def show_steps(self):
        print("""
        clf = LinearRegression()
        clf.fit(X_train, y_train)
        """)


    def works(self):
        print("It works!")

@pd.api.extensions.register_dataframe_accessor("Ensembles")
class Ensemblers(Base):

    def __init__(self, dataframe):
        super().__init__(dataframe)


    def enter_ensembles(self):
        print("Entered Ensembles. Success!!!!")
