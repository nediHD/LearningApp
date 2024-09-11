from tkinter import *
from views.tkinter.view import *
import json
from controllers.controller import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Test")
        self.geometry("700x450")
        self.state('zoomed')
        if get_amount_profiles() == 0:
            empty_data = {}
            filename = "whta_to_do.json"
            with open(filename, 'w') as file:
                json.dump(empty_data, file, indent=4)
            AddNewProfile(self)

        else:
            ChooseProfile(self)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def on_closing(self):
            # Create a pop-up window with a Yes/No question
            if messagebox.askyesno("Exit", "Did you clicked on job done ?"):
                self.destroy()  # Close the main window
            else:
                what_to_do.rotete_one_left(get_profile())
                self.destroy()
