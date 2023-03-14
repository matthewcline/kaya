from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from audios import app as audios_app
from images import app as images_app
import datetime
import json


@csrf_exempt 
def create_story(request):
    audio_file_path = request.POST.get('audio_file_path')
    transcript = request.POST.get('transcript')

    if audio_file_path:
        # transcript = audios_app.generate_transcript(audio_file_path)
        transcript = "test transcript"

    # image_path = images_app.generate_image_from_transcript(transcript)
    image_path = "test image path"

    # add user field
    story = {
        'date': str(datetime.datetime.now()),
        'transcript': transcript,
        'image_path': image_path
    }

    with open('kaya/stories.json') as f:
        data = f.read()

    stories = json.loads(data)
    stories.get("stories").append(story)

    with open('kaya/stories.json', "w") as f:
        json.dump(stories, f, indent=4)
    
    return JsonResponse(story)
