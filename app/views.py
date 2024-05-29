from django.shortcuts import render

# Create your views here.
from app.models import *

from django.http import HttpResponse

def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic created successfilly')
     
    return render(request,'insert_topic.html')


def insert_webpage(request):
    QLTO=Topic.objects.all()
    Webpages.objects.filter(topic_name='Tennis')
    d={'QLTO':QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        game=request.POST['game']
        email=request.POST['email']
        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpages.objects.get_or_create(topic_name=RTO,name=na,url=url,game=game,email=email)[0]
        WO.save()
        return HttpResponse('Webpage created successfully')
    
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    QLWO=Webpages.objects.all()
    d={'QLWO':QLWO}

    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']
        RWO=Webpages.objects.get(id=na)
        AO=AccessRecord.objects.get_or_create(name=RWO,date=da,author=au)[0]
        AO.save()
        return HttpResponse('AccessRecord created successfully')

    return render(request,'insert_accessrecord.html',d)


def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=Webpages.objects.none()
        for t in STL:
            WOS=WOS|Webpages.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpages.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)
