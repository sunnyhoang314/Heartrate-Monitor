import customtkinter as ctk
import tkinter as tk

# System settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Our app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Heartrate Monitor")

# Adding UI elements
title = ctk.CTkLabel(app, text="What is your name?")
title.pack(padx=10, pady=10)

# Name input
name_var = tk.StringVar()
name = ctk.CTkEntry(app, width=350, height=40, textvariable=name_var)
name.pack()

# Enter button
# enter = ctk.CTkButton(app, text="Enter", command=)

# Run app
app.mainloop()

