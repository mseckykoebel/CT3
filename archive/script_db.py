import json
import random


class ScriptDB:
    # later, this can be renamed to a more general db of more than just animals
    def __init__(self, path: str) -> None:
        # open and process file
        with open(path) as f:
            json_data = json.load(f)
            self.json_data = json_data
            self.animals = json_data["animals"]
            self.what_sentences = json_data["What sentences"]
            self.why_sentences = json_data["Why sentences"]
        # other inits
        self.current_animal = None
        self.current_description = None

    # set some random animal (pseudo-setter)
    def set_random_animal(self) -> str:
        # update the current animal to be a random choice inside of animals db
        self.current_animal = random.choices(self.animals)

    # concat a new animal to a what sentence
    def generate_what_sentence(self) -> str:
        # generate a random animal
        self.set_random_animal()
        random_what_sentence = random.choices(self.what_sentences)
        output = random_what_sentence + self.current_animal
        return "".join(output)

    """ 
    loop up the current animal, find the fact corresponding with it,
    and return the sentence
    """
    def generate_why_sentence(self) -> str:
        if self.current_animal is None:
            raise Exception("Error: current animal is null")
        current_animal = self.current_animal
        why_sentence = self.json_data["Why sentences"]["".join(current_animal)]
        return "".join(why_sentence)

    # find the current index of the animal (brute force and shitty)
    def current_animal_index(self) -> int:
        if self.current_animal is None:
            raise Exception("Error: current animal is null")
        for i in self.animals:
            if self.animals[i] == self.current_animal:
                return i
            else:
                return 0

    # boolean checker to see if some attribute is present in some collection
    def present_in_collection(self, item, collection) -> bool:
        for i in collection:
            if i in item:
                return True
            else:
                return False