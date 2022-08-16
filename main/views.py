from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video

def video_list(request):
  video_list = Video.objects.all()
  context = {'video_list': video_list}
  return render(request, 'video/video_list.html', context)
