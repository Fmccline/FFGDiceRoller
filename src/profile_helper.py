import json
from ffg_character import FFGCharacter


class ProfileHelper:

    PROFILE_FILE = "profiles.json"
    PROFILES = "profiles"
    CHARACTERS = "characters"
    NAME = "name"
    DICE = "dice"


    @staticmethod
    def get_profile_names():
        names = []
        with open(ProfileHelper.PROFILE_FILE) as json_file:
            data = json.load(json_file)
            profiles = data[ProfileHelper.PROFILES]
            for profile in profiles:
                names.append(profile[ProfileHelper.NAME])
        return names


    @staticmethod
    def load_profile(name):
        # returns a list of FFG characters given a profile name
        with open(ProfileHelper.PROFILE_FILE) as json_file:
            data = json.load(json_file)
            profiles = data[ProfileHelper.PROFILES]
            for profile in profiles:
                if profile[ProfileHelper.NAME] == name:
                    json_characters = profile[ProfileHelper.CHARACTERS]
                    return ProfileHelper.to_ffg_characters(json_characters)
        raise Exception("Uh oh, couldn't load the/a profile.")


    @staticmethod
    def to_ffg_characters(json_characters):
        # converts characters stored as json to FFG characters
        ffg_characters = []
        for json_character in json_characters:
            name = json_character[ProfileHelper.NAME]
            dice = json_character[ProfileHelper.DICE]
            ffg_character = FFGCharacter(name)                
            for die_type, die_amount in dice.items():
                ffg_character.set_dice(die_type, die_amount)
            ffg_characters.append(ffg_character)
        return ffg_characters


    @staticmethod
    def characters_to_json(characters):
        json_characters = []
        for character in characters:
            json_characters.append(ProfileHelper.character_to_json(character))
        return json_characters
        
    
    @staticmethod
    def character_to_json(character):
        dice = {}
        for die_type, die_amount in character.available_dice.items():
            if die_amount > 0:
                dice[die_type] = die_amount

        as_json = {}
        as_json[ProfileHelper.NAME] = character.name
        as_json[ProfileHelper.DICE] = dice
        return as_json


    @staticmethod
    def save_profile(name, characters):
        # give a list of FFGCharacters, saves them to a json profile with given name
        wrote = False
        json_characters = ProfileHelper.characters_to_json(characters)
        with open(ProfileHelper.PROFILE_FILE, "r+") as json_file:
            data = json.load(json_file)
            profiles = data[ProfileHelper.PROFILES]
            # check if profile exists and overwrite it
            for profile in profiles:
                if profile[ProfileHelper.NAME] == name:
                    profile[ProfileHelper.CHARACTERS] = json_characters
                    json_file.seek(0)
                    json.dump(data, json_file)
                    json_file.truncate()
                    wrote = True
            # create new profile since it doesnt exist
            if wrote is False:
                json_file.seek(0)
                profiles.append({ProfileHelper.NAME: name, ProfileHelper.CHARACTERS: json_characters})
                json.dump(data, json_file)
                json_file.truncate()

        