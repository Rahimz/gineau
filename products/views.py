from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Product, Image
from django.template import loader
from .forms import AddEmailForm
from taggit.models import Tag
from django.utils import timezone



def HomeView(request):
    products_w = Product.objects.filter(productGenre="women")
    products_m = Product.objects.filter(productGenre="men")
    
    form = AddEmailForm()
    if request.method == "POST":
        form = AddEmailForm(request.POST)        
        if form.is_valid():
            email = form.save(commit=False)
            email.date = timezone.now()
            email.save()                
    else:        
        form = AddEmailForm()

    return render(request,
                  'products/new_base.html',
                  {'products_w': products_w,
                  'products_m': products_m,
                   'form': form})

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:8:-1]


def ProductListView(request, genre=None, tag_slug=None):
    if genre in ('men', 'women'):
        products = Product.objects.filter(productGenre=genre)
    elif genre == None:
        products = Product.objects.all()
    else:
        raise Http404("Product does not exist")

    form = AddEmailForm()
    if request.method == "POST":
       form = AddEmailForm(request.POST)        
       if form.is_valid():
           email = form.save(commit=False)
           email.date = timezone.now()
           email.save()               
    else:        
        form = AddEmailForm()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    return render(request,
                  'products/products_list_w.html',
                  {'products': products,
                   'genre': genre,
                   'form': form,
                   'tag' : tag})


def add_email(req):
    form = AddEmailForm(req.POST)        
    if form.is_valid():
        email = form.save(commit=False)      
        email.save()
    else:        
        form = AddEmailForm()
    return form                   
                   

def DetailView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    form = AddEmailForm()
    if request.method == "POST":
       form = AddEmailForm(request.POST)        
       if form.is_valid():
           email = form.save(commit=False)
           email.date = timezone.now()
           email.save()               
    else:        
        form = AddEmailForm()

    return render(request,
                  'products/detail.html',                  
                  {'product': product,
                  'form': form,})



class blog(generic.ListView):
    template_name = 'products/blog.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:5:-1]
