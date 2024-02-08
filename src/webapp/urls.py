# Inside your Django app (e.g., webapp/urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path('vision/', views.vision, name='vision'),
    # path('history/', views.history, name='history'),
    # path('activities/', views.activities, name='activities'),
    # path('member-gallery/', views.member_gallery, name='member_gallery'),
    # path('weekly-reports/', views.weekly_reports, name='weekly_reports'),
]
