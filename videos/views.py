from django.shortcuts import render
from home.models import Video

def videopage(request):
    videos = Video.objects.all()
    context =  {'videos': videos}
    return render(request, "videopage.html", context)

def video(request, slugtwo):
    video = Video.objects.filter(slug=slugtwo).first()
    context = {'video':video}
    return render(request, "video.html", context)
