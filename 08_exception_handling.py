# Author: Allen Anker
# Created by Allen Anker on 2019-09-17

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))
finally:
    print('These lines are executed whatever happens')

print('Continue')


class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)
except MyInputError as err:
    print('error: {}'.format(err))
