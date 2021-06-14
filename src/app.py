import tkinter as tk
from main_view import MainView
from profile_helper import ProfileHelper


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.main_view = MainView(self)
        self.main_view.pack(side="top", fill="both", expand=True)
        self.main_view.grid_rowconfigure(0, weight=1)
        self.main_view.grid_columnconfigure(0, weight=1)
        self.create_profile_menu()

    def create_profile_menu(self):
        menubar = tk.Menu(self)
        profiles_menu = tk.Menu(menubar, tearoff=False)
        profiles = ProfileHelper.get_profile_names()
        for profile in profiles:
            profiles_menu.add_command(label=profile, command=lambda value=profile: self.main_view.set_profile(value))
        profiles_menu.add_separator()
        profiles_menu.add_command(label="Save Profile", command=lambda: self.save_profile())

        menubar.add_cascade(label = "Profiles", menu = profiles_menu)
        self.config(menu=menubar)

    def save_profile(self):
        characters = self.main_view.get_characters()
        profile_name = self.main_view.get_profile_name()
        ProfileHelper.save_profile(profile_name, characters)
        self.create_profile_menu()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = Application()
    app.mainloop()