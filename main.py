import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import sys

def execute_script():
    """Function to execute the main script logic"""
    print("Script execution started...")  # Add your customization logic here later
    root.destroy()  # Close the window after execution

# Create main window
root = ttk.Window(themename="darkly")
root.title("Windows Customization Script")
root.geometry("500x200")
root.resizable(False, False)

# Main frame container
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

# Heading label
label = ttk.Label(
    master=main_frame,
    text="Welcome to my Windows Customization Script!\nDo you want to execute the programs below?",
    font=('Segoe UI', 12),
    wraplength=400,
    justify='center'
)
label.pack(pady=10)

# Placeholder for program list
programs_label = ttk.Label(
    master=main_frame,
    text="[Program list will be added here]",
    font=('Segoe UI', 10),
    foreground='gray'
)
programs_label.pack(pady=5)

# Button container frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=15)

# Action buttons
yes_btn = ttk.Button(
    master=button_frame,
    text="Yes",
    command=execute_script,
    bootstyle=SUCCESS,
    width=10
)
yes_btn.grid(row=0, column=0, padx=5, sticky='w')

no_btn = ttk.Button(
    master=button_frame,
    text="No",
    command=lambda: sys.exit(),
    bootstyle=DANGER,
    width=10
)
no_btn.grid(row=0, column=1, padx=5, sticky='e')

# Configure grid columns for proper spacing
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# Center window on screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'+{x}+{y}')

# Start the GUI event loop
root.mainloop()
