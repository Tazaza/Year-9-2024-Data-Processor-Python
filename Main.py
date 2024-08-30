import tkinter as tk
from tkinter import filedialog, messagebox
import DataProcessor

# Function to load the file and calculate capacity
def calculate_capacity():
    file_path = file_entry.get()
    try:
        amp_hours_total = DataProcessor.calculateCapacity(file_path)
        result_label.config(text=f"Total capacity: {amp_hours_total:.2f}Ah")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open file dialog and select the file
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a data file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Initialize the main window
root = tk.Tk()
root.title("Data Processor")
root.geometry("400x300")

# Heading label
heading_label = tk.Label(root, text="Data Processor", font=("Arial", 16))
heading_label.pack(pady=10)

# File entry and browse button
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_entry = tk.Entry(file_frame, width=30)
file_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=5)

# Go button to calculate capacity
go_button = tk.Button(root, text="Go", command=calculate_capacity)
go_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
