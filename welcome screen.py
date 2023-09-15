import tkinter as tk
import os

def open_main_script():
    os.system('SPACE-DOC.exe')

def create_space_screen():
    root = tk.Tk()
    root.title("WELCOME TO SPACE-DOC🚀")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")  # Set window size to screen dimensions

    space_color = "#2d383a"  # New background color
    text_color = "white"     # White text color

    root.configure(bg=space_color)

    welcome_text = tk.Label(root, text="WELCOME TO SPACE-DOC🚀", font=("Helvetica", 36, "bold"), fg=text_color, bg=space_color)
    welcome_text.place(relx=0.5, rely=0.5, anchor="center")

    enter_button = tk.Button(root, text="Click here to enter", command=open_main_script, font=("Helvetica", 14), bg="black", fg="white")
    enter_button.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

create_space_screen()
