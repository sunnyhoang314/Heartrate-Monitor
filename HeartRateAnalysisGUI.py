import time
import threading
import subprocess
import customtkinter as ctk
import tkinter as tk

# Start the heart rate monitor script as a subprocess
subprocess.Popen(["python", 'HeartRateMonitor.py'])

# Function to continuously update the heart rate from the file
def updateHRA():
    global heart_rate
    while True:
        try:
            with open('pictures/hr.txt', 'r') as file:
                heart_rate = file.readline().strip()
        except:
            heart_rate = 'N/A'
        time.sleep(1)

# Thread for updating heart rate
heart_rate = '0'
heart_rate_thread = threading.Thread(target=updateHRA)
heart_rate_thread.daemon = True
heart_rate_thread.start()

# Function to record heart rate data during the countdown
def record_heart_rate_during_countdown(duration=60):
    heart_rate_data = []
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        heart_rate_data.append(heart_rate)
        time.sleep(1)
    # Write the recorded data to a new file
    with open('pictures/hr_record.txt', 'w') as file:
        for hr in heart_rate_data:
            file.write(f"{hr}\n")

# Function to analyze the heart rate data
def analyze_heart_rate():
    try:
        with open('pictures/hr_record.txt', 'r') as file:
            data = file.readlines()
            heart_rates = [int(hr.strip()) for hr in data if hr.strip().isdigit()]
            average_hr = sum(heart_rates) / len(heart_rates) if heart_rates else 0
            return average_hr
    except Exception as e:
        print(f"Error reading heart rate data: {e}")
        return None

# Function to display health summary
def health_summary(app, average_hr):
    if average_hr:
        if average_hr < 60:
            summary = "Heart rate is below average. If you're not a trained athlete, consider consulting a doctor."
        elif 60 <= average_hr <= 100:
            summary = "Heart rate is within the normal range."
        else:
            summary = "Heart rate is above average. Consider consulting a doctor if this is unexpected."
    else:
        summary = "Unable to analyze heart rate data."

    health_summary_text = ctk.CTkLabel(master=app,
                                       text=summary,
                                       width=120,
                                       height=25, 
                                       corner_radius=8)
    health_summary_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Main application function
def runHRA():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.geometry("600x480")
    app.title("Real-Time Data Reading")

    title = ctk.CTkLabel(master=app,
                 text="Click 'Start' to begin heart rate analysis, where the analysis will take\n1 minute worth of your heart rate data, and will then analyze the data to see where your health is at",
                 width=120, 
                 height=25, 
                 corner_radius=8,)
    title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    startButton = ctk.CTkButton(app, text="Start", command=lambda: [start_heart_rate(app), one_minute_text(app)])
    startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    app.mainloop()

# Function to start heart rate display
def start_heart_rate(app):
    global heart_rate
    heart_rate_text = ctk.CTkLabel(master=app,
                                   text="Current heartrate: " + str(heart_rate) + " BPM",
                                   width=120, 
                                   height=25, 
                                   corner_radius=8,)
    heart_rate_text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    def update_label():
        heart_rate_text.configure(text="Current heartrate: " + str(heart_rate) + " BPM")
        app.after(1000, update_label)

    update_label()

# Function to start the countdown and record heart rate
def one_minute_text(app):
    count_down_text = ctk.CTkLabel(master=app,
                                   text="Time remaining: 01:00",
                                   width=120,
                                   height=25, 
                                   corner_radius=8)
    count_down_text.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    def update_countdown(c=60):
        if c > 0:
            m, s = divmod(c, 60)
            count_down_text.configure(text="Time remaining: {:02d}:{:02d}".format(m, s))
            app.after(1000, update_countdown, c-1)
        else:
            count_down_text.configure(text="Time's up!")
            # Call the analyze_heart_rate function and display the health summary
            average_hr = analyze_heart_rate()
            health_summary(app, average_hr)

    # Start the countdown and record the heart rate data
    update_countdown()
    threading.Thread(target=record_heart_rate_during_countdown, args=(60,)).start()

if __name__ == "__main__":
    runHRA()
