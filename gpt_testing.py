import openai
import os
from dotenv import load_dotenv

# TODO
import chronological

# set up the environment
load_dotenv("gpt.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def generate_something():
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt="What are some key points I should know when studying the ottoman empire?\n\n1.",
        temperature=1,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text


def marv_the_robot():
    response = openai.Completion.create(
        engine="davinci",
        prompt="Marv is a chatbot that reluctantly answers questions.\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: Why is the blue whale so big?\nMarv:",
        temperature=0.3,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["\n\n"],
    )
    return response.choices[0].text

print(marv_the_robot())
