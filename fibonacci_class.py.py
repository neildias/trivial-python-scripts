class fibonacci:
    a, b = 0, 1

    def _fibonacci_error(self, x):
        try:
            if x < 1: return True
        except:
            return True

    def erase_stored_values(self):
        fibonacci.a, fibonacci.b = 0, 1

    def fibonacci_generator(self):
        fibonacci.a, fibonacci.b = fibonacci.b, fibonacci.a + fibonacci.b
        while True:
            yield fibonacci.b

    def get_reusable_fibonacci(self, endNum):
        '''Returns index and the corresponding fibonacci number as a dictionary'''
        if self._fibonacci_error(endNum): return "Invalid input! Input must be positive integers."
        fibonacci_db = {1: 0, 2: 1}
        for fibonacci_index in range(3, endNum + 1):
            fibonacci_db[fibonacci_index] = next(self.fibonacci_generator())
        self.erase_stored_values()
        return fibonacci_db

    def fibonacci_recurcive(self, n=10, first_pass=True, fibonacci_db=None):
        '''This does not store values hence memory used is neglibible'''
        if self._fibonacci_error(n): return "Invalid input! Input must be positive integers."
        global a, b

        # first pass logic
        if first_pass and n == 2: return [0, 1]
        if first_pass and n == 1: return [0]
        if not fibonacci_db:
            fibonacci_db = [0, 1]
        else:
            fibonacci_db = fibonacci_db

        # recursion terminator clause
        if n == 0:
            self.erase_stored_values()
            return fibonacci_db
        if first_pass:
            print("{} {}".format(a, b), end=" ")
            n -= 2
        a, b = b, a + b
        print(b, end=" ")
        fibonacci_db.append(b)
        return self.fibonacci_recurcive(n - 1, first_pass=False, fibonacci_db=fibonacci_db)

    def get_ith_fibonacci(self, n):
        # use get_reusable_fibonacci
        if self._fibonacci_error(n): return "Invalid input! Input must be positive integers."
        for index in range(3, n + 1):
            number = next(self.fibonacci_generator())
            # n-1 as python indexing starts from zero
            if index == n:
                self.erase_stored_values()
                return number

    def get_upto_ith_fibonacci(self, x):
        if self._fibonacci_error(x): return "Invalid input! Input must be positive integers."
        return self.get_reusable_fibonacci(x)

    def is_fibonacci(self, x):
        if self._fibonacci_error(x): return "Invalid input! Input must be positive integers."
        num = 0
        while num < x:
            num = next(self.fibonacci_generator())
            if num == x:
                self.erase_stored_values()
                return f"Yes, {x} is a fibonacci number."
        self.erase_stored_values()
        return f"No, {x} is NOT a fibonacci number."

    def sample(self, x=10):
        return self.get_upto_ith_fibonacci(x)

    def get_this_Index_Range(self, lowerIndex, higherIndex):
        if self._fibonacci_error(lowerIndex): return "Invalid input! Input must be positive integers."
        if self._fibonacci_error(higherIndex): return "Invalid input! Input must be positive integers."

        if lowerIndex == higherIndex or higherIndex < lowerIndex:
            return "Invalid input both numbers must de unique."

        #depending on the lower number, counter and the fibonacci_db are initiated
        if lowerIndex == 1: counter, fibonacci_db = 2, {1: 0, 2: 1}
        elif lowerIndex == 2: counter, fibonacci_db = 1, {2:1}
        else: counter, fibonacci_db = 3, {}

        if higherIndex == 1: return fibonacci_db
        for index in range(3, higherIndex + 1):
            fib_num = next(self.fibonacci_generator())
            if index >= lowerIndex:
                fibonacci_db[index] = fib_num
        self.erase_stored_values()
        return fibonacci_db

    def get_this_number_Range(self, lowerNum, higherNum):
        if self._fibonacci_error(lowerNum): return "Invalid input! Input must be positive integers."
        if self._fibonacci_error(higherNum): return "Invalid input! Input must be positive integers."
        if lowerNum == higherNum or higherNum < lowerNum:
            return "Invalid input both numbers must de unique."

        # depending on the lower number, counter and the fibonacci_db are initiated
        if lowerNum == 1: counter, fibonacci_db = 2, {1: 0, 2: 1}
        elif lowerNum == 2: counter, fibonacci_db = 1, {2: 1}
        else: counter, fibonacci_db = 3, {}

        if higherNum == 1: return fibonacci_db
        while True:
            fib_num = next(self.fibonacci_generator())
            if fib_num > higherNum:
                self.erase_stored_values()
                return fibonacci_db
            if fib_num >= lowerNum:
                fibonacci_db[counter] = fib_num
            counter += 1

    def _num_converter(self, num, num2=0):
        try:
            num = int(float(num))
            num2 = int(float(num2))
            if num2: return num, num2
            return num
        except:
            print("Wrong Input! Number(s) must be positive integers.")

    def menu(self):
        print("Welcome to the fibonacci solver app. Let us know which operation "
              "from the following you wish to use...")
        print("""
        1. Get a sample of the fibonacci series.
        2. Get a dictionary of fibonacci series upto a particular index.
        3. Get the ith fibonacci series.
        4. Get fibonacci series from range of index x to index y.
        5. Get fibonacci numbers occuring between x and y (not indexes but actual numbers).
        6. Check if a particular number is a fibonacci number.
        """)
        try:
            selection = int(input("Type the selection. Eg. type 1 for the first option."))
            if selection < 1 or selection > 6:
                return "Invalid Entry"
        except:
            return "Invalid Entry."
        if selection in (2, 3, 6):
            # question for 1 num input
            number = input("Please enter the number per the operation you selected : ")
            number = self._num_converter(number)
            if selection == 2:
                print(self.get_upto_ith_fibonacci(number))
            elif selection == 3:
                print(self.get_ith_fibonacci(number))
            else:
                print(self.is_fibonacci(number))
        elif selection in (4, 5):
            # get double input
            lower = input("Please enter the lower number per the operation you selected : ")
            higher = input("Please enter the higher number per the operation you selected : ")
            lower, higher = self._num_converter(lower, higher)
            if selection == 4:
                print(self.get_this_Index_Range(lower, higher))
            else:
                print(self.get_this_number_Range(lower,higher))
        else:
            print(self.get_upto_ith_fibonacci(15))

