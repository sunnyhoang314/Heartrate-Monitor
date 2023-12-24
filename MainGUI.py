import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk


# System settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Our app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Heartrate Monitor")

# Adding UI elements
title = ctk.CTkLabel(master=app, 
                     text="Welcome to Heartrate Monitor! Please choose your session:", 
                     width=120, 
                     height=25, 
                     corner_radius=8,)
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Adding buttons for session type
rtdrImage = ctk.CTkImage(Image.open("pictures/big-data-7216839_1280.png"), size=(60, 60))
rtdrButton = ctk.CTkButton(app, text="Real-Time Data Reading", image=rtdrImage)
rtdrButton.place(relx=0.05, rely=0.4, anchor=tk.NW)

dvImage = ctk.CTkImage(Image.open("pictures/dual-access-chart.png"), size=(60, 60))
dvButton = ctk.CTkButton(app, text="Data Visualization", image=dvImage)
dvButton.place(relx=0.497, rely=0.4, anchor=tk.N)

hraImage = ctk.CTkImage(Image.open("pictures/health-insights-heart-rate.png"), size=(90, 60))
hraButton = ctk.CTkButton(app, text="Heart Rate Analysis", image=hraImage)
hraButton.place(relx=0.95, rely=0.4, anchor=tk.NE)

asImage = ctk.CTkImage(Image.open("pictures/1200px-OOjs_UI_icon_alert_destructive.svg.png"), size=(60, 60))
asButton = ctk.CTkButton(app, text="Alert System", image=asImage)
asButton.place(relx=0.25, rely=0.7, anchor=tk.SW)

dlImage = ctk.CTkImage(Image.open("pictures/3155997.png"), size=(60, 60))
dlButton = ctk.CTkButton(app, text="Data Logging", image=dlImage)
dlButton.place(relx=0.65, rely=0.7, anchor=tk.S)


# Name input
# name_var = tk.StringVar()
# name = ctk.CTkEntry(app, width=350, height=40, textvariable=name_var)
# name.pack()

# Enter button
# enter = ctk.CTkButton(app, text="Enter", command=)

# Run app
app.mainloop()

