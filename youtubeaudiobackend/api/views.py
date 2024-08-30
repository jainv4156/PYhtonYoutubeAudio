from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from pytubefix import YouTube

import os


# Create your views here.

@api_view(['GET'])
def audio(request):
    if request.method == 'GET':
        request_url = request.GET.get('url')
        myvideo = YouTube(request_url)
        output_directory = '/home/vaibhav-jain/Desktop/Newfolder/PYhtonYoutubeAudi/youtubeaudiobackend/audios'
        mystrems=myvideo.streams.filter(only_audio=True,progressive=False).order_by('filesize')
        filename=mystrems[0].title
        filepath=mystrems[0].download(output_path=output_directory,filename=filename)


        if os.path.exists(filepath):
            return FileResponse(open(filepath, 'rb'), content_type='audio/mp4')
        else:
            return Response({"error": "File not found"}, status=404)

@api_view(['GET']) 
def demoRequest(request):
    return Response({"message":"Hello, world. You're at the polls index."})