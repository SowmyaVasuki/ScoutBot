from .models import *
from django.shortcuts import render
import time
import socket

from django.http import HttpResponse
# Create your views here.

def index(request):
	template = 'livestream/index.html'
	return render(request,template,{})

def forward(request):
	print("forward")
	return HttpResponse('forward')

def reverse(request):
	print("reverse")
	return HttpResponse('reverse')

def right(request):
	print("right")
	return HttpResponse('right')

def left(request):
	print("left")
	return HttpResponse('left')

def forward1(request):
	print("forward1")
	return HttpResponse('forward1')

def reverse1(request):
	print("reverse1")
	return HttpResponse('reverse1')

def right1(request):
	print("right1")
	return HttpResponse('right1')

def left1(request):
	print("left1")
	return HttpResponse('left1')

def stop(request):
	print("stop")
	return HttpResponse('stop')

def checkfor(request):
	print("checkfor")
	return HttpResponse('checkfor')

def checkback(request):
	print("checkback")
	return HttpResponse('checkback')