class LoginException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class LoginIdNotFoundException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NullException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)