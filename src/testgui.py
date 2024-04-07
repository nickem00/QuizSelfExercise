import tkinter as tk
from PIL import Image, ImageTk

class SimpleImageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bildtest")
        self.master.geometry("400x400")

        try:
            # Ladda bilden
            self.background_image = Image.open("../data/background.png")
            self.background_image = ImageTk.PhotoImage(self.background_image)

            # Skapa en Label och sätt bilden
            self.image_label = tk.Label(self.master, image=self.background_image)
            self.image_label.pack(fill="both", expand=True)

            # Behåll en referens till bilden inom Label-objektet
            self.image_label.image = self.background_image
        except Exception as e:
            print(f"Kunde inte ladda bilden: {e}")

SimpleImageGUI(tk.Tk()).master.mainloop()
