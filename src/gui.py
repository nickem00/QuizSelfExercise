import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
# import game
import log_writer
# import time
import login_gui


class GUI:

    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.root.title("Quiz Game")
        self.root.geometry("500x650+950+100")
        self.root.resizable(False, False)
        self.root.config(bg="#755035")
        self.icon_url = ("../assets/media/icon.ico")
        # C:/users/nicke/IdeaProjects/QuizSelfExercise/assets/media/icon.ico
        self.root.iconbitmap(self.icon_url)
        self.login_screen()
        self.log_writer = log_writer.Log_writer()

    def login_screen(self):
        self.custom_font = font.Font(family="Impact", size=60, weight="bold")

        self.title_url = ("../assets/media/title.png")
        self.title_image = ImageTk.PhotoImage(Image.open(self.title_url)
                                              .resize(
                                               (500, 200), Image.Resampling.
                                               LANCZOS))
        self.title_label = tk.Label(self.root, image=self.title_image)
        self.title_label.image = self.title_image
        self.title_label.place(x=0, y=50, relwidth=1, relheight=0.3)

        self.button_frame = tk.Frame(self.root, bg="#755035")
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.register_button = tk.Button(self.button_frame,
                                         text="Register",
                                         font=("Impact", 30),
                                         bg="#FFD700",
                                         fg="#000000",
                                         width=10,
                                         command=self.register_screen)
        self.register_button.grid(row=0, column=0)
        self.login_button = tk.Button(self.button_frame,
                                      text="Login",
                                      font=("Impact", 30),
                                      bg="#FFD700",
                                      fg="#000000",
                                      width=10,
                                      command=self.user_login)
        self.login_button.grid(row=0, column=1)
        self.button_frame.place(x=0, y=300, relwidth=1, relheight=0.15)
        self.quit_button = tk.Button(self.root,
                                     text="Quit",
                                     font=("Impact", 30),
                                     bg="#b32700",
                                     fg="#000000",
                                     command=self.quit)
        self.quit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def quit(self):
        self.log_writer.write_log("Quitting the game")
        self.root.quit()

    def register_screen(self):

        # Hide the main menu buttons
        self.button_frame.place_forget()
        self.quit_button.place_forget()

        # Create the registration frame
        self.registration_frame = tk.Frame(self.root, bg="#755035")
        self.username_entry = tk.Entry(self.registration_frame,
                                       font=("Impact", 20))
        self.password_entry = tk.Entry(self.registration_frame,
                                       font=("Impact", 20), show="*")
        self.registration_frame.columnconfigure(0, weight=1)
        self.username_entry.grid(row=0, column=0, pady=(0, 40))
        self.password_entry.grid(row=1, column=0, pady=(0, 40))
        self.registration_frame.place(x=0, y=300, relwidth=1, relheight=0.3)

        # Create the registration labels
        self.username_entry_label = tk.Label(self.root,
                                             text="Username",
                                             font=("Impact", 14),
                                             bg="#755035",
                                             fg="#FFD700")
        self.password_entry_label = tk.Label(self.root,
                                             text="Password",
                                             font=("Impact", 14),
                                             bg="#755035",
                                             fg="#FFD700")
        self.username_entry_label.place(x=104, y=266)
        self.password_entry_label.place(x=104, y=346)

        # Create the registration buttons
        self.registation_buttons_frame = tk.Frame(self.root,
                                                  bg="#755035")
        self.registation_buttons_frame.columnconfigure(0, weight=1)
        self.registation_buttons_frame.columnconfigure(1, weight=1)
        self.submit_button = tk.Button(self.registation_buttons_frame,
                                       text="Submit",
                                       font=("Impact", 20),
                                       bg="#FFD700",
                                       fg="#000000",
                                       width=10,
                                       command=self.sumbit_registration_button)
        self.back_button = tk.Button(self.registation_buttons_frame,
                                     text="Back",
                                     font=("Impact", 20),
                                     bg="#FFD700",
                                     fg="#000000",
                                     width=10,
                                     command=self.back_from_registration)
        self.back_button.grid(row=0, column=0)
        self.submit_button.grid(row=0, column=1)
        self.registation_buttons_frame.place(x=0, y=500, relwidth=1, relheight=0.3)

    def back_from_registration(self):
        if hasattr(self, "error_message_label"):
            self.error_message_label.place_forget()
        self.registation_buttons_frame.place_forget()
        self.registration_frame.place_forget()
        self.username_entry_label.place_forget()
        self.password_entry_label.place_forget()
        self.login_screen()

    def successful_registration(self):
        self.registation_buttons_frame.place_forget()
        self.registration_frame.place_forget()
        self.username_entry_label.place_forget()
        self.password_entry_label.place_forget()

        self.successful_registration_label = tk.Label(self.root,
                                                      text="Registration successful",
                                                      font=("Impact", 20),
                                                      bg="#755035",
                                                      fg="#23eb00")
        self.successful_registration_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        self.login_screen()

    def sumbit_registration_button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Username: {username}, Password: {password}")
        successfull = self.game.register_new_user(username, password)
        if successfull is True:
            print("User registered successfully")
            self.log_writer.write_log(f"User <{username}> registered "
                                      "successfully.")

            self.successful_registration()
        else:
            print("User registration failed")
            self.log_writer.write_log("User registration "
                                      f"for <{username}> failed.")
            self.show_error_message("Username already exists or is invalid.\n"
                                    "Please choose another.")

    def show_error_message(self, message):
        self.error_message_label = tk.Label(self.root,
                                            text=message,
                                            font=("Arial", 15),
                                            bg="#755035",
                                            fg="#FF0000")
        self.error_message_label.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

    def user_login(self):
        login_gui.Login_GUI(self.root, self.game)
