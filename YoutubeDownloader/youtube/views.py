from django.shortcuts import render ,HttpResponse ,redirect
from pytube import YouTube
from datetime import datetime
import os
from .tasks import  *
from django.conf import settings
from django.http import JsonResponse 
import json


def home(request):
	if request.method=='POST':
		url = request.POST.get('url')
		data = get_video_info(url)
		return JsonResponse(data,safe=False)
	return render(request,'youtube_app/home.html')

def download_ready(request):
	if request.method == 'POST':
		print('under download_ready section..')
		try:
			yt = YouTube(request.POST.get('url'))
			video = yt.streams.filter(progressive=True,res=request.POST.get('res')).first()
			current_date = datetime.now()
			temp_dir ='{}{}{}/{}/'.format(settings.BASE_DIR,settings.MEDIA_URL,settings.TEMP_DIR,current_date)
			if not os.path.exists(temp_dir):
				os.makedirs(temp_dir)
			clear_dir.delay(temp_dir)
			video.download(temp_dir)
			filepath = '{}/{}'.format(current_date,os.listdir(temp_dir)[0])
		except Exception as e:
			print(e)
		return JsonResponse({'status' : 1,'path' : filepath})

def get_video_info(url):
	try:
		info = {}
		yt = YouTube(url)
		info['status'] = 1
		info['title'] = yt.title
		info['thumbnail_url'] = yt.thumbnail_url
		info['video_avilable'] = [i.resolution for i in yt.streams.filter(progressive=True) ]
		info['url'] = url
				
	except Exception as e:
		info['status'] = 0
		info['message'] = f'URL not found -- Exception {e}'
	finally:
		return info




