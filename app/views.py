from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Swetha(request):
    return HttpResponse('<h1><marque>Hi Swetha How are you </h1></marquee>')
def raji(request):
    return HttpResponse('<h1><marquee>Hi raji waste fellow em dng</h1></marquee>')
def dhana(request):
    return HttpResponse('<h1><marquee>dhana is mentalfellow thikkalafellow</h1></marquee>')