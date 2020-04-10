from django.shortcuts import render

def home(request):
	return render(request,'youtube_app/home.html')