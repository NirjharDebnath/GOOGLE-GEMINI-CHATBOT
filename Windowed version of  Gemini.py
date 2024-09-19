import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Dark Mode Input/Output GUI")
root.geometry("600x400")  # Set window size

# Define dark mode styles
dark_bg = "#1e1e1e"       # Dark background
dark_fg = "#ffffff"       # Light text
input_bg = "#2e2e2e"      # Slightly lighter background for input area
output_bg = "#3e3e3e"     # Slightly lighter background for output area
highlight_color = "#007acc"  # A blue highlight color

# Configure the overall window background to dark
root.configure(bg=dark_bg)

# Create the input Text widget (for user input)
input_text = tk.Text(root, height=10, bg=input_bg, fg=dark_fg, insertbackground=dark_fg, 
                     font=("Consolas", 14), padx=10, pady=10, wrap=tk.WORD, bd=0)
input_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Create a label to divide Input and Output areas
divider_label = ttk.Label(root, text="Output", background=dark_bg, foreground=highlight_color, font=("Arial", 12, "bold"))
divider_label.pack(pady=5)

# Create the output Text widget (for output display)
output_text = tk.Text(root, height=10, bg=output_bg, fg=dark_fg, insertbackground=dark_fg, 
                      font=("Consolas", 14), padx=10, pady=10, wrap=tk.WORD, bd=0, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Function to handle input/output interaction (for demonstration)
def process_input():
    # Get input text
    input_content = input_text.get("1.0", tk.END).strip()

    # Clear the output area and insert processed text
    output_text.config(state=tk.NORMAL)  # Enable editing in output area
    output_text.delete("1.0", tk.END)  # Clear previous output
    output_text.insert(tk.END, f"Processed Output:\n{input_content}")  # Process and display input
    output_text.config(state=tk.DISABLED)  # Disable editing in output area

# Add a button to trigger input processing
process_button = tk.Button(root, text="Process Input", command=process_input, 
                           bg=highlight_color, fg=dark_fg, font=("Arial", 12, "bold"), bd=0)
process_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
