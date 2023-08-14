from django.urls import path

from catalog.views import home, contact_info

urlpatterns = [
    path('', home, name='home'),
    path('contact_info/', contact_info, name='contact_info'),
]
