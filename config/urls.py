from django.urls import path, include

urlpatterns = [
    path('calc-week/', include('main.urls')),
]
