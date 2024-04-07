import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.con_info = {
            "host": "localhost",
            "user": "root",
            "password": "15Delta715!",
            "database": "quiz_game"
        }
        self.connection = None
    
    def add_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO user_credentials (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            print(f"Användare {username} har lagts till i databasen")
        except mysql.connector.Error as e:
            print("Fel vid tillägg av användare: ", e)
        finally:
            cursor.close()
            

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.con_info)
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Ansluten till MySQL Server version ", db_info)
        except mysql.connector.Error as e:
            print("Fel vid anslutning till MySQL: ", e)

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Anslutningen till MySQL är stängd")
