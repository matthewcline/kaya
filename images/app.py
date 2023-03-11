import urllib.request
from . import api

def generate_image(prompt):
    url = api.generate_image(prompt)
    image_location = save_image(url, "/Users/matthewcline/Downloads/", "")
    return image_location

def save_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

def generate_image_prompt(transcript):
    return f"Generate a concise prompt to provide to the open ai \
            image generation model from the following story: {transcript}.  \
            Make sure it uses a colored pencil drawing style."
