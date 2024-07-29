import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Define a dictionary with application names, their Steam URLs, and icons
# Use absolute paths to ensure icons are found
base_dir = os.path.dirname(os.path.abspath(__file__))
applications = {
    'Call of Duty: Black Ops': {'url': 'steam://rungameid/42700', 'icon': os.path.join(base_dir, 'black_ops_icon.ico')},
    'Call of Duty: Black Ops Multiplayer': {'url': 'steam://rungameid/42710', 'icon': os.path.join(base_dir, 'black_ops_mp_icon.ico')},
}

class GameLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BO1 Launcher by Spyral")
        self.geometry("500x400")  # Adjusted window size for better spacing
        self.resizable(False, False)
        self.configure(bg='black')

        self.script_path = os.path.abspath(sys.argv[0])
        self.command_text = f'"{self.script_path}" %COMMAND%'

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Add a title label
        self.title_label = tk.Label(self, text="BO1 Launcher by Spyral", font=('FSP DEMO - Bank Gothic BT Light', 16), pady=10, bg='black', fg='white')
        self.title_label.pack()

        # Add a description label
        self.description_label = tk.Label(self, text="Choose an Application to Launch", font=('FSP DEMO - Bank Gothic BT Light', 14), pady=10, bg='black', fg='white')
        self.description_label.pack()

        # Create a frame to contain the buttons
        button_frame = tk.Frame(self, bg='black')
        button_frame.pack(pady=15, fill=tk.X)

        for app_name, app_info in applications.items():
            frame = tk.Frame(button_frame, bg='black')
            frame.pack(pady=10, fill=tk.X)

            # Check if the icon file exists
            if not os.path.exists(app_info['icon']):
                logging.error(f"Icon file not found: {app_info['icon']}")
                messagebox.showerror("Error", f"Icon file not found: {app_info['icon']}")
                continue

            # Validate the Steam URL
            if not re.match(r'^steam://rungameid/\d+$', app_info['url']):
                logging.error(f"Invalid Steam URL: {app_info['url']}")
                messagebox.showerror("Error", f"Invalid Steam URL: {app_info['url']}")
                continue

            icon_image = Image.open(app_info['icon'])
            icon_image = icon_image.resize((32, 32), Image.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon_image)

            # Create a frame for the icon and button to ensure they are aligned properly
            icon_button_frame = tk.Frame(frame, bg='black')
            icon_button_frame.pack(padx=10)

            icon_label = tk.Label(icon_button_frame, image=icon_photo, bg='black')
            icon_label.image = icon_photo  # Keep a reference to avoid garbage collection
            icon_label.pack(side=tk.LEFT)

            launch_button = tk.Button(icon_button_frame, text=app_name, font=('FSP DEMO - Bank Gothic BT Light', 12), bg='#ADD8E6', fg='black', command=lambda url=app_info['url']: self.launch_app(url))
            launch_button.pack(side=tk.LEFT, padx=10)

        # Button to copy the command to clipboard
        self.copy_button = tk.Button(self, text="Copy Command to Clipboard", font=('FSP DEMO - Bank Gothic BT Light', 12), bg='#ADD8E6', fg='black', command=self.copy_command)
        self.copy_button.pack(pady=10)

        # Button to show instructions
        self.show_message_button = tk.Button(self, text="Show Instructions", font=('FSP DEMO - Bank Gothic BT Light', 12), bg='#ADD8E6', fg='black', command=self.show_instructions)
        self.show_message_button.pack(pady=10)

    def launch_app(self, url):
        # Try to launch the application and close the window
        try:
            logging.debug(f"Launching URL: {url}")
            os.startfile(url)
            self.destroy()  # Close the application window
        except Exception as e:
            logging.error(f"Failed to launch application: {e}")
            messagebox.showerror("Error", f"Failed to launch application: {e}")

    def show_instructions(self):
        message_text = f"If you want this launcher to open up when you launch BO1 on Steam, go to the launch options of BO1 and type:\n\n\"{self.command_text}\""
        messagebox.showinfo("Instructions", message_text)

    def copy_command(self):
        # Copy the command text to the clipboard
        self.clipboard_clear()
        self.clipboard_append(self.command_text)
        self.update()  # Update the clipboard
        messagebox.showinfo("Copied", "Command has been copied to clipboard.")

if __name__ == "__main__":
    app = GameLauncher()
    app.mainloop()
