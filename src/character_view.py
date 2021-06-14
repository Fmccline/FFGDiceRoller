from dice import Dice
import tkinter as tk


class FFGCharacterView:
    
    def __init__(self, frame, character, row, on_delete):
        self.frame = frame
        self.ffg_character = character
        self.row = row
        self.dice_entries = self.make_dice_entries()
        self.name_entry = self.make_name_entry()

        self.delete_btn = tk.Button(frame, text="Delete", command=lambda: on_delete(self))
        self.delete_btn.grid(row=row, column=len(self.dice_entries.keys()) + 1)

    def make_name_entry(self):
        name_entry = tk.Entry(self.frame, justify='center')
        name_entry.grid(row=self.row, column=0, padx=10)
        self.delete_then_insert(name_entry, self.ffg_character.name)
        return name_entry

    def make_dice_entries(self):
        dice_entries = {}   
        dice_types = Dice.dice_types()
        for idx in range(len(dice_types)):
            die_type = dice_types[idx]
            entry = tk.Entry(self.frame, justify='center')
            entry.grid(row=self.row, column=idx+1, padx=10)
            self.delete_then_insert(entry, self.ffg_character.get_dice(die_type))
            dice_entries[die_type] = entry
        return dice_entries

    def delete_then_insert(self, entry, text):
        while(len(entry.get()) > 0):
            entry.delete(0)
        entry.insert(0, text)

    def get_name(self):
        return self.name_entry.get()

    def get_character(self):
        self.ffg_character.set_name(self.get_name())
        for die_type, entry in self.dice_entries.items():
            die_amount = int(entry.get())
            self.ffg_character.set_dice(die_type, die_amount)
        return self.ffg_character

    def destroy(self):
        for entry in self.dice_entries.values():
            entry.destroy()
        self.delete_btn.destroy()