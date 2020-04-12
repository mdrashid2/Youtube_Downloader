from django.shortcuts import render ,HttpResponse
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

def download_ready(request):
	if request.method == 'POST':
		print('under download_ready section..')
		try:
			yt = YouTube(request.POST.get('url'))
			video = yt.streams.filter(progressive=True,res=request.POST.get('res')).first()
			temp_dir ='{}{}{}/{}/'.format(settings.BASE_DIR,settings.MEDIA_URL,settings.TEMP_DIR,datetime.now())
			print(temp_dir)
			if not os.path.exists(temp_dir):
				os.makedirs(temp_dir)
			video.download(temp_dir)
		except Exception as e:
			print(e)
		return JsonResponse({'status' : 1,'path' : '{}{}.mp4'.format(temp_dir,yt.title)})

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
		info['message'] = 'URL not found'
	finally:
		return info



# def download(request):
# 	if request.method=='POST':
# 	    file_path = request.POST.get('path')
# 	    if os.path.exists(file_path):
# 	        with open(file_path, 'rb') as fh:
# 	            response = HttpResponse(fh.read(), content_type="application/force-download")
# 	            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
# 	            return response
# 	    raise Http404
# 	else:
# 		return redirect('home_page')

