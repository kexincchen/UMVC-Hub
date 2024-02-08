from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def home(request):
#     return render(request, 'home.html')

# def vision(request):
#     return render(request, 'vision.html')

# def history(request):
#     return render(request, 'history.html')

# def activities(request):
#     return render(request, 'activities.html')

# def member_gallery(request):
#     return render(request, 'member_gallery.html')

# def weekly_reports(request):
#     # This view will later include logic to check if a user is logged in and has member access
#     return render(request, 'weekly_reports.html')
