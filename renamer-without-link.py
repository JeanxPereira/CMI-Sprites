import tkinter as tk
from tkinter import ttk

# create a function to process the input and generate the output
def process_input():
    input_list = input_box.get("1.0", "end").splitlines()
    output_list = []

    for item in input_list:
        # extract the name, variant, and image URL from the input item
        if "[x] " in item and "!" in item:
            name = item.split("[x] ")[1].split(" !")[0].title()
            if "(" in name and ")" in name:
                variant = name.split("(")[1].split(")")[0]
                name = name.split("(")[0].strip()
            else:
                variant = ""
            image_url = item.split("![](")[1].split(")")[0]

            # create the output item string with a maximum length of 30 characters for the first column
            if variant:
                output_item = f"| {name[:25].ljust(28)} ({variant}) | :white_check_mark: |![]({image_url})|"
            else:
                output_item = f"| {name[:25].ljust(28)} | :white_check_mark: |![]({image_url})|"
            output_list.append(output_item)

    # display the output in the output box
    output_box.delete("1.0", "end")
    output_box.insert("1.0", "\n".join(output_list))


# create the GUI
root = tk.Tk()
root.title("List Converter / Renamer PRO")
root.iconbitmap("icon.ico")
root.configure(bg="#141823")

# set the style for the GUI
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#141823", foreground="white")
style.configure("TEntry", background="#232a3b", foreground="white", fieldbackground="#232a3b")
style.configure("Accent.TButton", background="#7F5AF0", foreground="white", padding=10, width=10)
style.configure("Danger.TButton", background="#F05454", foreground="white", padding=10, width=10)
style.configure("Primary.TButton", background="#E1E1E6", foreground="#141823", padding=10, width=10)
style.map("TButton", background=[('active', '#444c63')], foreground=[('active', 'white')])

# create the input box
input_label = ttk.Label(root, text="Input:")
input_label.pack(padx=10, pady=10)
input_box = tk.Text(root, height=10, width=50, bg="#232a3b", fg="white", highlightbackground="#232a3b", highlightcolor="#232a3b", bd=0)
input_box.pack(padx=10, pady=10)

# define the Omni theme colors
bg = "#191622"
fg = "#E1E1E6"
accent = "#7F5AF0"
select_bg = "#9D7EFC"
select_fg = "#191622"

# create the output box
output_label = ttk.Label(root, text="Output:")
output_label.pack(padx=10, pady=10)
output_box = tk.Text(root, height=10, width=50, bg="#232a3b", fg="white", highlightbackground="#232a3b", highlightcolor="#232a3b", bd=0)
output_box.pack(padx=10, pady=10)

# create the process button
process_button = ttk.Button(root, text="Process", command=process_input, style="Accent.TButton", width=20, cursor="hand2")
process_button.pack(pady=10)

# create the clear button
clear_button = ttk.Button(root, text="Clear", command=lambda: input_box.delete("1.0", "end"), style="Danger.TButton")
clear_button.pack(side="left", padx=10, pady=10)

# create the exit button
exit_button = ttk.Button(root, text="Exit", command=root.destroy, style="Primary.TButton", cursor="hand2")
exit_button.pack(side="right", padx=10, pady=10)

# set the focus on the input box
input_box.focus()

# disable window resizing
root.resizable(False, False)

# run the GUI loop
root.mainloop()