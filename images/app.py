import urllib.request
from . import api

def generate_image(prompt):
    url = api.generate_image(prompt)
    print("image url: ", url)
    image_location = save_image(url, "/Users/matthewcline/Downloads/", "")
    return {
        'image_url': url,
        'local_url': image_location
    }

def save_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

def generate_image_prompt(transcript):
    
    return f"Generate a concise prompt to provide to the open ai \
            image generation model from the following story: '{transcript}'.  \
            Make sure it uses a colored pencil drawing style."

def generate_image_from_transcript(transcript):
    image_prompt = generate_image_prompt(transcript)
    image_url, local_url = generate_image(image_prompt)
    print({
        'image_prompt': image_prompt,
        'image_url': image_url,
        'local_url': local_url
    })
    return {
        'image_prompt': image_prompt,
        'image_url': image_url,
        'local_url': local_url
    }
