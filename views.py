from django.shortcuts import render
from pytube import YouTube


def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_lowest_resolution()

        # downloads video
        stream.download()

        # returning HTML page
        return render(request, 'index.html')
    return render(request, 'index.html')