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
    def register_new_user(self, username, password):
        print("Registering new user..")
        try:
            # see if the database has a user with the same username
            # if not, add the user to the database
            self.db_manager.connect()
            self.db_manager.add_user(username, password)
            successfull = True
        except Exception as e:
            successfull = False
            print(f"Error: {e}")
        finally:
            self.db_manager.disconnect()
            return successfull
        # self.db_manager.connect()
        # self.db_manager.add_user("test", "test")
        # self.db_manager.disconnect()

    def login_user(self):
        print("Login user")

    def start_game(self):
        pass