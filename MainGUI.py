import customtkinter as ctk
from PIL import Image
import tkinter as tk
from HeartRateAnalysisGUI import *
from DataVisualizationGUI import *
from AlertSystemGUI import *
from DataVisualizationGUI import *
from RealTimeDataReadingGUI import *


# System settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Our app frame
app = ctk.CTk()
app.geometry("600x480")
app.title("Heartrate Monitor")

# Adding UI elements
title = ctk.CTkLabel(master=app, 
                     text="Welcome to Heartrate Monitor! Please choose your session:", 
                     width=120, 
                     height=25, 
                     corner_radius=8,)
title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Adding buttons for session type
rtdrImage = ctk.CTkImage(Image.open("pictures/big-data-7216839_1280.png"), size=(100, 100))
rtdrButton = ctk.CTkButton(app, text="Real-Time Data Reading", image=rtdrImage, command=runRTDR)
rtdrButton.place(relx=0.05, rely=0.2, anchor=tk.NW)

dvImage = ctk.CTkImage(Image.open("pictures/dual-access-chart.png"), size=(100, 100))
dvButton = ctk.CTkButton(app, text="Data Visualization", image=dvImage, command=runDV)
dvButton.place(relx=0.76, rely=0.2, anchor=tk.N)

hraImage = ctk.CTkImage(Image.open("pictures/health-insights-heart-rate.png"), size=(130, 100))
hraButton = ctk.CTkButton(app, text="Heart Rate Analysis", image=hraImage, command=runHRA)
hraButton.place(relx=0.05, rely=0.6, anchor=tk.W)

asImage = ctk.CTkImage(Image.open("pictures/1200px-OOjs_UI_icon_alert_destructive.svg.png"), size=(130, 100))
asButton = ctk.CTkButton(app, text="Alert System", image=asImage, command=runAS)
asButton.place(relx=0.95, rely=0.6, anchor=tk.E)

# Run app
app.mainloop()

