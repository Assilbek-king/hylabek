from django.shortcuts import render
from main.models import *
# Create your views here.

def indexHandler(request):
    cats = Category.objects.all()
    tovars = Tovar.objects.all()
    photos = Photo.objects.all()
    feeds = Feedback.objects.all()
    otzivs = Otziv.objects.all()
    services = Service.objects.all()

    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        feed.comment = request.POST.get('comment')
        feed.categoriya = request.POST.get('categoriya')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')


    return render(request, 'index.htm', {
        'cats': cats,
        'tovars': tovars,
        'photos': photos,
        'feeds': feeds,
        'otzivs': otzivs,
        'services': services,
    })


def indexkzHandler(request):
    cats = Category.objects.all()
    tovars = Tovar.objects.all()
    photos = Photo.objects.all()
    feeds = Feedback.objects.all()
    otzivs = Otziv.objects.all()

    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        feed.comment = request.POST.get('comment')
        feed.categoriya = request.POST.get('categoriya')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')


    return render(request, 'index2.html', {
        'cats': cats,
        'tovars': tovars,
        'photos': photos,
        'feeds': feeds,
        'otzivs': otzivs,
    })


