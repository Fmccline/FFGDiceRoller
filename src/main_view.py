import tkinter as tk
from character_view import FFGCharacterView
from profile_helper import ProfileHelper
from ffg_character import FFGCharacter


class MainView(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.profile_text = tk.StringVar()
        self.create_header()
        self.character_views = []
        self.create_character_views()

    def create_header(self):
        self.winfo_toplevel().title("Star Wars Dice Roller")

        profile_label = tk.Label(self, text="Profile: ")
        profile_entry = tk.Entry(self, textvariable=self.profile_text)
        profile_label.grid(row=0, column=0)
        profile_entry.grid(row=0, column=1)

        add_character_btn = tk.Button(self, text="Add Character", command=self.add_character_view)
        add_character_btn.grid(row=1, column=0, columnspan=2, pady=5)

        header_texts = ["Character Name", "Green Dice", "Yellow Dice", "Blue Dice", "Purple Dice", "Red Dice", "Black Dice", "Remove"]
        for idx in range(len(header_texts)):
            header = tk.Label(self, text=header_texts[idx])
            header.grid(row=2, column=idx, padx=10) 

    def set_profile(self, profile):
        self.character_views = []
        self.profile_text.set(profile)
        self.create_character_views(profile)

    def create_character_views(self, profile_name=None):
        characters = []
        if profile_name is None:
            characters = [FFGCharacter(char) for char in ['A','B','C','D']]
        else:
            characters = ProfileHelper.load_profile(profile_name)
        for character in characters:
            self.add_character_view(character)
    
    def add_character_view(self, character=None):
        if character is None:
            character = FFGCharacter("New Character")
        character_view = FFGCharacterView(self, character, len(self.character_views)+3, self.delete_character_view)
        self.character_views.append(character_view)

    def delete_character_view(self, character_view):
        character_view.destroy()
        self.character_views.remove(character_view)

    def get_characters(self):
        characters = []
        for character_view in self.character_views:
            characters.append(character_view.get_character())
        return characters

    def get_profile_name(self):
        return self.profile_text.get()



