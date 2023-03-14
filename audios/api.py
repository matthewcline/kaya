import os
import openai
import requests

def generate_transcript(path):
	# example path: "/Users/matthewcline/Downloads/March_10_2023.m4a"
	audio_file= open(path, "rb")
	transcript = openai.Audio.transcribe("whisper-1", audio_file)
	return transcript

