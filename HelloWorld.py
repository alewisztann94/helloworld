import numbers

# HelloWorld application to test AWS CodeBuild

class HelloWorld:
    def __init__(self):
        self.message = 'Hello world!'

    '''
    Given two numbers return True if a > b
    '''
    def isgt(self, a, b):

        if not isinstance(a, numbers.Number):
            raise ValueError

        if not isinstance(b, numbers.Number):
            raise ValueError


        if a > b:
            return True
        else:
            return False

