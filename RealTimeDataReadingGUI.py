import customtkinter as ctk
import time
import threading
import subprocess
import tkinter as tk

# Start the heart rate monitor script as a subprocess
subprocess.Popen(["python", 'HeartRateMonitor.py'])

def runRTDR():
    # System settings
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    # Our app frame
    app = ctk.CTk()
    app.geometry("600x480")
    app.title("Real-Time Data Reading")

    title = ctk.CTkLabel(master=app,
                 text="Click 'Start' to begin the real time data reading session",
                 width=120, 
                 height=25, 
                 corner_radius=8,)
    title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Start button
    startButton = ctk.CTkButton(app, text="Start", command=updateRTDR)
    startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Run app
    app.mainloop()

# Function to continuously update the heart rate from the file
def updateRTDR():
    global heart_rate
    while True:
        try:
            with open('pictures/hr.txt', 'r') as file:
                heart_rate = file.readline().strip
        except:
            heart_rate = 'N/A'
        time.sleep(1)

# Thread for updating heart rate
heart_rate = '0'
heart_rate_thread = threading.Thread(target=updateRTDR)
heart_rate_thread.daemon = True
heart_rate_thread.start()