import requests
from images import generate_image, generate_image_prompt

def create_story(transcript):
    prompt = generate_image_prompt(transcript)
    url = generate_image(prompt)

    # save url

