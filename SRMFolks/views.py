from django.shortcuts import render,redirect

# Create your views here.

def homePage(request):
    return render(request, 'homePage.html')


def eventsPage(request):
    return render(request, 'eventsPage.html')

def announcementsPage(request):
    return render(request, 'announcementsPage.html')

def galleryPage(request):
    return render(request, 'galleryPage.html')

def communityPage(request):
    return render(request, 'communityPage.html')

def logoutPage(request):
    redirect('homePage')