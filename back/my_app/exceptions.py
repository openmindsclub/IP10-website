

class EmailAlreadyExistError(Exception):
    """Exception is raised when email adress already exis in the database"""

    def __init__(self, email):
        self.email = email

    def __str__(self):
        return "the email {} already exist in the database, use a PUT request to update user informations".format(self.email)

class InvalidActivityError(Exception):
    """Exception is raised when an invalide activity has been entered"""

    def __init__(self, activity):
        self.activity = activity

    def __str__(self):
        return "the activity {} isn't accepted".format(self.activity)
