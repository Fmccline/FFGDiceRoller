import tkinter as tk
from character_view import FFGCharacterView
from ffg_character import FFGCharacter


class RollsView(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.rolls_button = tk.Button(text="Roll")
        self.rolls_button.pack()