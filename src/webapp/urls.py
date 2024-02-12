# Inside your Django app (e.g., webapp/urls.py)
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "web"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(template_name="webapp/login.html"), name="login"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path('vision/', views.vision, name='vision'),
    # path('history/', views.history, name='history'),
    # path('activities/', views.activities, name='activities'),
    # path('member-gallery/', views.member_gallery, name='member_gallery'),
    path("reports/", views.ReportsView.as_view(), name="reports"),
    path("reports/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("reports/<int:report_id>/update", views.update_report, name="update_report"),
]
