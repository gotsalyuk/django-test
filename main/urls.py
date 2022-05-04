from django.urls import path, re_path
from main.views import main_page




urlpatterns = [
    re_path('$', main_page)
]


