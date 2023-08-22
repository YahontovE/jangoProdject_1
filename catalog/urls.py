from django.urls import path

from catalog.views import home, contact_info, product

urlpatterns = [
    path('', home, name='home'),
    path('contact_info/', contact_info, name='contact_info'),
    path('<int:pk>/product/', product, name='product'),
]
