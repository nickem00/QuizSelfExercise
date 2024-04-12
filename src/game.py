import database_manager
import log_writer

class Game:

    def __init__(self):
        self.db_manager = database_manager.DatabaseManager()
        self.log_writer = log_writer.Log_writer()

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

    """
    A method that logs the user into the game.

    The method takes a username and password as arguments and checks
    whether the username and password match the username and password
    in the database. If the username and password match, the method returns
    True. If the username and password do not match, the method returns False.
    """
    def login_user(self, username, password):
        print(f"Trying to log in user {username}..")
        self.log_writer.write_log(f"Trying to log in user {username}..")
        try:
            self.db_manager.connect()
            user = self.db_manager.get_user(username)
            if user is None:
                print(f"User {username} not found.")
                self.log_writer.write_log(f"User {username} not found.")
                return False
            if user[1] == password:
                print(f"User {username} logged in.")
                self.log_writer.write_log(f"User {username} logged in.")
                return True
            else:
                print(f"Worng password entered for user {username}.")
                self.log_writer.write_log(f"Wrong password entered for user {username}.")
                return False
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db_manager.disconnect()
        return False

    def start_game(self):
        pass