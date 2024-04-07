import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import game

class GUI:

    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.root.title("Quiz Game")
        self.root.geometry("500x650+950+100")
        self.root.resizable(False, False)
        self.root.config(bg="#755035")
        self.root.iconbitmap("../assets/media/icon.ico")
        self.main_menu()

    def main_menu(self):
        self.custom_font = font.Font(family="Impact", size=60, weight="bold")

        self.title_image = ImageTk.PhotoImage(Image.open("../assets/media/title.png").resize((500, 200), Image.Resampling.LANCZOS))
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
                                         command=self.game.register_new_user)
        self.register_button.grid(row=0, column=0)
        self.login_button = tk.Button(self.button_frame,
                                      text="Login",
                                      font=("Impact", 30),
                                      bg="#FFD700",
                                      fg="#000000",
                                      width=10,
                                      command=self.game.login_user)
        self.login_button.grid(row=0, column=1)
        self.button_frame.place(x=0, y=300, relwidth=1, relheight=0.3)
        self.quit_button = tk.Button(self.root,
                                     text="Quit",
                                     font=("Impact", 30),
                                     bg="#b32700",
                                     fg="#000000",
                                     command=self.root.quit)
        self.quit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def register_screen(self):
        self.registration_frame = tk.Frame(self.root, bg="#755035")
        self.username_entry = tk.Entry(self.registration_frame,
                                       font=("Impact", 20))
        self.password_entry = tk.Entry(self.registration_frame,
                                       font=("Impact", 20))
        self.submit_button = tk.Button(self.registration_frame,
                                       text="Submit",
                                       font=("Impact", 20),
                                       bg="#FFD700",
                                       fg="#000000",
                                       command=self.game.register_new_user)
        self.back_button = tk.Button(self.registration_frame,
                                     text="Back",
                                     font=("Impact", 20),
                                     bg="#FFD700",
                                     fg="#000000",
                                     command=self.main_menu)
        self.username_entry.grid(row=0, column=0)
        self.password_entry.grid(row=1, column=0)
        self.submit_button.grid(row=2, column=0)
        self.registration_frame.place(x=0, y=300, relwidth=1, relheight=0.3)
