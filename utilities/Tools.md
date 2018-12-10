class Switcher(object):
    def numbers_to_months(self, argument):
        """Dispatch method"""
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def month_1(self):
        return "January"
 
    def month_2(self):
        return "February"
 
    def month_3(self):
        return "March"


def zero():
    return "zero"
 
def one():
    return "one"
 
def two():
    return "two"
 
switcher = {
        0: zero,
        1: one,
        2: two
    }
 
"""
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
Input: numbers_to_strings(1)
Output: One
 
Input: switcher[1]=two #changing the switch case
Input: numbers_to_strings(1)
Output: Two
"""