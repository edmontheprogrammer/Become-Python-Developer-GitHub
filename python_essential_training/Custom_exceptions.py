# Custom Exceptions
# Creating a custom exception is basically making a class that inherits from the
# general built-in 'Exception' class. Then you can add additional functions and
# attributes to the Custom class you create.

class CustomException(Exception):
    pass


def causeError():
    raise CustomException('You called the causeError function!')


causeError()


# Adding Attributes
class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(
            f'Status code: {self.statusCode} and message is {self.message}')


class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'


class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'


def raiseServerError():
    raise ServerError()


raiseServerError()
