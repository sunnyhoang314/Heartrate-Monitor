import time
import threading
import subprocess
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Start the heart rate monitor script as a subprocess
subprocess.Popen(["python", 'HeartRateMonitor.py'])

# Function to continuously update the heart rate from the file
def updateDV(heart_rate_list, start_time_list):
    while True:
        try:
            with open('pictures/hr.txt', 'r') as file:
                heart_rate = int(file.readline().strip())
        except:
            heart_rate = 0
        heart_rate_list.append(heart_rate)
        start_time_list.append(datetime.now())
        time.sleep(1)

def animate(i, heart_rate_list, plot):
    plot.clear()
    plot.plot(heart_rate_list)
    plot.set_xlabel('Time (seconds)')
    plot.set_ylabel('Heart Rate (BPM)')

def export_graph(heart_rate_list, start_time_list):
    # Save the graph as an image
    plt.figure(figsize=(10, 6))
    plt.plot(start_time_list, heart_rate_list, label='Heart Rate (BPM)')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate (BPM)')
    plt.title('Heart Rate Data')
    plt.legend()
    plt.savefig('heart_rate_graph.png')
    print("Heart rate graph saved to heart_rate_graph.png")

def runDV():
    # Our app frame
    app = tk.Tk()
    app.geometry("600x480")
    app.title("Data Visualization")

    title = tk.Label(app,
                     text="Click 'Start' to begin the real time data reading session")
    title.pack()

    # Heart rate list and start time list
    heart_rate_list = []
    start_time_list = []

    # Thread for updating heart rate
    heart_rate_thread = threading.Thread(target=updateDV, args=(heart_rate_list, start_time_list))
    heart_rate_thread.daemon = True

    # Start button
    startButton = tk.Button(app, text="Start", command=heart_rate_thread.start)
    startButton.pack()

    # Export button
    exportButton = tk.Button(app, text="Export Graph", command=lambda: export_graph(heart_rate_list, start_time_list))
    exportButton.pack()

    # Create a new figure and plot
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)

    # Create a canvas and add it to the app
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Animation for updating the plot
    ani = animation.FuncAnimation(fig, animate, fargs=(heart_rate_list, plot), interval=1000)

    # Run app
    app.mainloop()
