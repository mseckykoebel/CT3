import openai
import os
from dotenv import load_dotenv

# set up the environment
load_dotenv("gpt.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def main():
    """
    Used primarily for testing
    """
    print(f"Random animal: {get_animal()}")
    # test generation
    animal_1 = "horse"
    animal_2 = "tyrannosaurus rex"
    print(random_name_generator())
    print(get_single_why(animal_1))
    print(get_comparison_why(animal_1, animal_2))
    print(get_insane_comparison_why(animal_1, animal_2))


def get_animal() -> str:
    """
    Prompt asks for a common animal. Returns an animal at random in the form of a string.
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt="I am a trivia-loving bot. If you ask me to name an animal, I will give you the name of an animal.\n\n\nInput: Name an animal\nOutput:",
        temperature=0.9,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        stop=["\n"],
    )
    animal = response.choices[0].text.replace('"', "")
    # this is pretty much just filtering
    if (
        (not animal.strip().isalpha())
        or (len(animal.split()) > 2)
        or (chr(65533) in animal)
    ):
        return get_animal()

    # removing 'a ' so like 'a dog' will turn into just 'dog'
    if animal[0:2] == "a ":
        animal = animal[2:]
    elif animal[0:3] == "an ":
        animal = animal[3:]
    return animal


def get_single_why(arg: str) -> str:
    """
    Function that takes arg1 and returns a string explaining why that argument would make a good pet
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt=f'I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery or has no clear answer, I will respond with "I just think their cool, honestly".\n\nInput: Can you tell me something good about why the {arg} is a good pet?\nOutput:',
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.7,
        stop=["\n"],
    )
    if (
        len(response.choices[0].text) < 20
        or response.choices[0].text == "I just like them, IDK"
    ):
        print("recurse")
        return get_single_why(arg)
    else:
        return response.choices[0].text


def get_comparison_why(arg1: str, arg2: str) -> str:
    """
    Function that takes arg1, and explains why it would be a better pet than arg2
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt=f'I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery or has no clear answer, I will respond with "I just think their cool, honestly".\n\nInput: Why is the {arg2} a better pet than than the {arg1}?\nOutput:',
        temperature=0.4,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )
    if (
        len(response.choices[0].text) < 20
        or response.choices[0].text == "I just think their cool, honestly"
    ):
        print("recurse")
        return get_comparison_why(arg1, arg2)
    else:
        return response.choices[0].text


def get_insane_comparison_why(arg1: str, arg2: str) -> str:
    """
    Function that takes arg1, and explains why it would be a better pet than arg2
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt=f'I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery or has no clear answer, I will respond with "I just think their cool, honestly".\n\nInput: Why is the {arg2} a better pet than than the {arg1}?\nOutput:',
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.9,
        presence_penalty=0.7,
        stop=["\n"],
    )
    if (
        len(response.choices[0].text) < 20
        or response.choices[0].text == "I just think their cool, honestly"
    ):
        print("recurse")
        return get_insane_comparison_why(arg1, arg2)
    else:
        return response.choices[0].text


def random_name_generator() -> str:
    response = openai.Completion.create(
        engine="davinci",
        prompt="This is a random name generator\n\nRandom name: David\nRandom name: Sophia\nRandom name: Grace:\nRandom name:",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    return response.choices[0].text


if __name__ == "__main__":
    main()
