import tkinter as tk
from tkinter import filedialog
from main import apply_filters_to_batch
from resize import batch_resize
from rename import batch_rename
from compress import batch_compress
from filters import apply_filter
from compress import batch_export

def run_batch_processing():
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    
    # Get user choice for filter and format
    filter_type = filter_var.get()
    format_type = format_var.get()
    
    apply_filters_to_batch(input_folder, output_folder, filter_type)
    batch_resize(output_folder, output_folder, size=(800, 800))
    batch_rename(output_folder, new_name="final_image")
    batch_compress(output_folder, output_folder, quality=80)
    batch_export(output_folder, output_folder, new_format=format_type)

# Create the main window
root = tk.Tk()
root.title("Creative Batch Processor")

# Filter options
filter_var = tk.StringVar(value="grayscale")
filter_label = tk.Label(root, text="Choose Filter:")
filter_label.pack()

filters = ["grayscale", "sepia", "blur", "brightness", "contrast"]
for f in filters:
    tk.Radiobutton(root, text=f.capitalize(), variable=filter_var, value=f).pack()

# Format options
format_var = tk.StringVar(value="JPEG")
format_label = tk.Label(root, text="Choose Export Format:")
format_label.pack()

formats = ["JPEG", "PNG", "BMP"]
for f in formats:
    tk.Radiobutton(root, text=f, variable=format_var, value=f).pack()

# Run Button
run_button = tk.Button(root, text="Run Batch Processing", command=run_batch_processing)
run_button.pack()

# Start the GUI loop
root.mainloop()
