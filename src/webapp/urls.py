# Inside your Django app (e.g., webapp/urls.py)
from django.urls import path
from . import views

app_name = "web"
urlpatterns = [
    path("", views.home, name="home"),
    # path('vision/', views.vision, name='vision'),
    # path('history/', views.history, name='history'),
    # path('activities/', views.activities, name='activities'),
    # path('member-gallery/', views.member_gallery, name='member_gallery'),
    path("reports/", views.reports, name="reports"),
    path("reports/<int:report_id>/", views.detail, name="detail"),
]
