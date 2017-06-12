from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
import sys
sys.path.append('./DB')
from login import *
from profile import *

def audio(request):
	audio = open('./Sound/test.wav','rb')
	return HttpResponse(audio, content_type = 'audio/mpeg')

def image(request):
	image = open('./trips/test.png','rb')
	return FileResponse(image)

def username(request):
	return JsonResponse({"title": "isLoginSuccess","user_id":"Allen"})

def getusername(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	print (user_id)
	user_name = getUserName(user_id)
	print (user_name)
	return JsonResponse({"title":"getUserName","name":user_name})

def setuservoice(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	#undone

def getuservoice(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	print (user_id)
	filename = getUserVoice(user_id)
	print (filename)
	audio = open(filename,'rb')
	return HttpResponse(audio, content_type = 'audio/mpeg')

def setuserphoto(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	#undone

def testp():
	print (getUserPhoto('1'))

def getuserphoto(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	print (info)
	filename = getUserPhoto(user_id)
	print (filename)
	image = open(filename,'rb')
	return FileResponse(image)

def isloginsuccess(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	password = info[3]
	print (user_id,password)
	result = isLoginSuccess(user_id, password)
	print (result)
	if result == True:
		return JsonResponse({"title": "isLoginSuccess","result":"True"})
	else:
		return JsonResponse({"title": "isLoginSuccess","result":"False"})
# Create your views here.

def setuseraccount(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	password = info[3]
	print (user_id,password)
	result = setUserAccount(user_id,password)
	print (result)
	if result == True:
		return JsonResponse({"title": "setUserAccount","result":"True"})
	else: 
		return JsonResponse({"title": "setUserAccount","result":"False"})

def changepassword(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	new_password = info[3]
	print (user_id,new_password)
	result = changePassword(user_id,new_password)
	print (result)
	if result == True:
		return JsonResponse({"title": "changePassword","result":"True"})
	else: 
		return JsonResponse({"title": "changePassword","result":"False"})

# def getuserinformation(request):
# 	info = request.META['PATH_INFO'].strip().split('/')
# 	print (info)
# 	user_id = info[0]
# 	name,photo,voice = getUserInformation(user_id)
# 	return JsonResponse({"title": "getUserInformation","name":name,"photo":photo,"voice":voice})

def setuserphoto(request):
	info = request.META['PATH_INFO'].strip().split('/')
	user_id = info[2]
	print (user_id)
	result = setUserPhoto(user_id,test_photo)
	print (result)
	if result == "True":
		return JsonResponse({"title":'setUserPhoto',"result":"True"})
	else:
		return JsonResponse({"title":'setUserPhoto',"result":"False"})

def test_setuserphoto(request):
	a = open('./trips/test.png','rb')
	l = 0
	f = ""
	for line in a:
		if l == 0:
			f = line
			l = 1
		else:
			f += line
	setUserPhoto('a',f)
	return JsonResponse({"title":'setUserPhoto',"result":"True"})

def test_setuservoice(request):
	a = open('./trips/test.wav','rb')
	l = 0
	f = ""
	for line in a:
		if l == 0:
			f = line
			l = 1
		else:
			f += line
	setUserVoice('a',f)
	return JsonResponse({"title":'setUserVoice',"result":"True"})

def testing():
	print (setUserPhoto("b","c"))

def setuservoice(request):
	info = request.META['PATH_INFO'].split('/')
	user_id = info[0]
	sound = info[1]
	print (user_id,sound)
	result = setUserVoice(user_id,photo)
	print (result)
	if result == "True":
		return JsonResponse({"title":'setUserVoice',"result":"True"})
	else:
		return JsonResponse({"title":'setUserVoice',"result":"False"})
# name (string), photo (Binary string), sound (Binary string)
# True/False (Bool)
# True/False (Bool)
def getNearbyPin(request):
	info = request.META['PATH_INFO'].split('/')
	latitude = info[0]
	longitude = info[1]

def getNearbyPinByTag(request):
	info = request.META['PATH_INFO'].split('/')
	latitude = info[0]
	longitude = info[1]
	tag = info[2]

def getSoundBysound_id(request):
	info = request.META['PATH_INFO'].split('/')
	sound_id = info[0]

def storeSound(request):
	info = request.META['PATH_INFO'].split('/')
	latitude = info[0]
	longitude = info[1]
	user_id = info[2]
	title = info[3]
	description = info[4]
	date = info[5]
	tag = info[6]

def deleteSound(request):
	info = request.META['PATH_INFO'].split('/')
	sound_id = info[0]

def changeSoundInformation(request):
	info = request.META['PATH_INFO'].split('/')
	title = info[0]
	description = info[1]
	tag = info[2]
# getNearbyPin	latitude	longitude						
# getNearbyPinByTag	latitude	longitude	tag					
# getSoundBysound_id	sound_id							
# storeSound	latitude	longitude	user_id	sound	title	description	date	tag
# deleteSound	sound_id							
# changeSoundInformation	title	description	tag					




