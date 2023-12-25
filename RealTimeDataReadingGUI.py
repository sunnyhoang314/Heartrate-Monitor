import customtkinter as ctk
import tkinter as tk

def runRTDR():
    # System settings
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    # Our app frame
    app = ctk.CTk()
    app.geometry("600x480")
    app.title("Real-Time Data Reading")

    # Run app
    app.mainloop()