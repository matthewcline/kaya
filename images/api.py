import os
import openai
import requests

def generate_image(prompt):
  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
  )
  image_url = response['data'][0]['url']
  return image_url

def generate_image_prompt(prompt):
  # TODO: call chatgpt