from django.shortcuts import render 
from pytube import YouTube
from datetime import datetime
import os
from django.conf import settings
from django.http import JsonResponse 
import json

def home(request):
	if request.method=='POST':
		url = request.POST.get('url')
		data = get_video_info(url)
		return JsonResponse(data,safe=False)
	return render(request,'youtube_app/home.html')

def download_video(url):
	try:
		yt = YouTube(url)
		temp_dir ='{}/{}/{}'.format(settings.BASE_DIR,settings.TEMP_DIR,datetime.now())
		if not os.path.exists(temp_dir):
			os.makedirs(temp_dir)
	except Exception as e:
		print(e)

def get_video_info(url):
	try:
		info = {}
		yt = YouTube(url)
		info['status'] = 1
		info['title'] = yt.title
		info['thumbnail_url'] = yt.thumbnail_url
		info['video_avilable'] = [i.resolution for i in yt.streams.filter(progressive=True) ]
				
	except Exception as e:
		info['status'] = 0
		info['message'] = e
	finally:
		return info
