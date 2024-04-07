import database_manager

class Game:

    def __init__(self):
        self.db_manager = database_manager.DatabaseManager()

    """
    This method is called when the user clicks the "Register" button
    in the GUI. It first changes the gui to the register screen and
    then checks whether the user has entered a valid and unique username
    and password. If the user has entered a valid username and password,
    the user is added to the database. If the user has entered an invalid
    username or password, the user is prompted to enter a valid username
    and password. If the user has entered a username that already exists
    in the database, the user is prompted to enter a unique username.
    """
    def register_new_user(self):
        print("Registering new user..")
        
        # self.db_manager.connect()
        # self.db_manager.add_user("test", "test")
        # self.db_manager.disconnect()

    def login_user(self):
        print("Login user")

    def start_game(self):
        pass