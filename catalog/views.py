from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'семейный магазин'
    }
    template_name = 'catalog/home.html'


def contact_info(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_info.html', context)


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'семейный магазин',
    }
    template_name = 'catalog/product.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content',)
    success_url = reverse_lazy('catalog:list')
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content',)
    #success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail',args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list')
