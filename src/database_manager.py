import mysql.connector
import log_writer


class DatabaseManager:
    def __init__(self):
        self.con_info = {
            "host": "localhost",
            "user": "root",
            "password": "15Delta715!",
            "database": "quiz_game"
        }
        self.connection = None
        self.log_writer = log_writer.Log_writer()

    def add_user(self, username, password):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"INSERT INTO user_credentials (username, password) "
                           f"VALUES ('{username}', '{password}')")
            self.connection.commit()
            print(f"User <{username}> added to database")
            self.log_writer.write_log(f"User <{username}> added to database")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.log_writer.write_log(f"Error: {e}")
            raise e
        finally:
            cursor.close()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.con_info)
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Ansluten till MySQL Server version ", db_info)
                self.log_writer.write_log(f"Connected to MySQL Server version "
                                          f"{db_info}")
        except mysql.connector.Error as e:
            print("Fel vid anslutning till MySQL: ", e)
            self.log_writer.write_log(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Anslutningen till MySQL är stängd")
            self.log_writer.write_log("Connection to MySQL is closed")

    def get_user(self, username):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM user_credentials WHERE username = '{username}'")
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.log_writer.write_log(f"Error: {e}")
            raise e
        finally:
            cursor.close()
