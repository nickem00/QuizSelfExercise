import tkinter as tk
# from tkinter import font
from PIL import Image, ImageTk
import database_manager
import log_writer


class Login_GUI:

    def __init__(self, root, game):
        self.root = root
        self.root.title("Quiz Game")
        self.log_writer = log_writer.Log_writer()
        self.db_manager = database_manager.DatabaseManager()
        self.game = game
        self.icon_url = ("../assets/media/icon.ico")
        self.root.iconbitmap(self.icon_url)
        self.show_login_screen()

    def show_login_screen(self):
        self.login_screen()

    def login_screen(self):
        # Add a #755035-colored background to the login screen to
        # hide the previous screen
        self.background = tk.Label(self.root, bg="#755035")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_url = ("../assets/media/title.png")
        self.title_image = ImageTk.PhotoImage(Image.open(self.title_url)
                                              .resize(
                                               (500, 200), Image.Resampling.
                                               LANCZOS))
        self.title_label = tk.Label(self.root, image=self.title_image)
        self.title_label.image = self.title_image
        self.title_label.place(x=0, y=50, relwidth=1, relheight=0.3)

        # Create the login frame
        self.login_frame = tk.Frame(self.root, bg="#755035")
        self.username_entry = tk.Entry(self.login_frame,
                                       font=("Impact", 20))
        self.password_entry = tk.Entry(self.login_frame,
                                       font=("Impact", 20), show="*")
        self.login_frame.columnconfigure(0, weight=1)
        self.username_entry.grid(row=0, column=0, pady=(0, 40))
        self.password_entry.grid(row=1, column=0, pady=(0, 40))
        self.login_frame.place(x=0, y=300, relwidth=1, relheight=0.3)

        # Create the login labels
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

        # Create the login buttons
        self.login_buttons_frame = tk.Frame(self.root,
                                            bg="#755035")
        self.login_buttons_frame.columnconfigure(0, weight=1)
        self.login_buttons_frame.columnconfigure(1, weight=1)
        self.login_button = tk.Button(self.login_buttons_frame,
                                      text="Login",
                                      font=("Impact", 20),
                                      bg="#FFD700",
                                      fg="#000000",
                                      width=10,
                                      command=self.login_button)
        self.back_button = tk.Button(self.login_buttons_frame,
                                     text="Back",
                                     font=("Impact", 20),
                                     bg="#FFD700",
                                     fg="#000000",
                                     width=10,
                                     command=self.back_button)
        self.back_button.grid(row=0, column=0)
        self.login_button.grid(row=0, column=1)
        self.login_buttons_frame.place(x=0, y=500, relwidth=1, relheight=0.3)

    def back_button(self):
        self.hide_login_screen()

    def hide_login_screen(self):
        self.login_frame.place_forget()
        self.username_entry_label.place_forget()
        self.password_entry_label.place_forget()
        self.login_buttons_frame.place_forget()
        self.background.place_forget()
        self.title_label.place_forget()

    def login_button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.game.login_user(username, password)
