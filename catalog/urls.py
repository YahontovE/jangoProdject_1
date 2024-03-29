from django.urls import path

from catalog.views import contact_info, ProductListView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact_info/', contact_info, name='contact_info'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('create/',BlogCreateView.as_view(), name='create'),
    path('list/',BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('create_product/',ProductCreateView.as_view(), name='create_product'),
]
