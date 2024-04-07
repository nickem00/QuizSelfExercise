import tkinter as tk
from gui import GUI
from game import Game

def main():
    root = tk.Tk()
    app = GUI(root, Game())
    root.mainloop()

if __name__ == "__main__":
    main()