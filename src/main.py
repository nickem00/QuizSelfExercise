import tkinter as tk
from gui import GUI
from game import Game
import log_writer


def main():
    root = tk.Tk()
    app = GUI(root, Game())
    log_writer.Log_writer().clear_log()
    root.mainloop()


if __name__ == "__main__":
    main()
