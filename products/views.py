from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Product
from django.template import loader
from .forms import AddEmailForm
from taggit.models import Tag
from django.utils import timezone


def add_email(req):
    form = AddEmailForm(req.POST)        
    if form.is_valid():
        email = form.save(commit=False)      
        email.save()
    else:        
        form = AddEmailForm()
    return form

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
        products = get_object_or_404(Product, productGenre=genre)
    elif genre == None:
        products = Product.objects.all()
        # products = get_object_or_404(Product)
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
                  'form': form})


def add_new_email(request):
    pass
    # products_w = Product.objects.filter(productGenre="women")
    # products_m = Product.objects.filter(productGenre="men")
    # if request.method == "POST":        
    #     form = AddEmailForm(request.POST)        
    #     if form.is_valid():
    #         email = form.save(commit=False)      
    #         email.save()
    #         # return redirect('/')   

    # else:        
    #     form = AddEmailForm()

    # return render(request,
    #             'products/new_base.html',
    #             {'products_w': products_w,
    #             'products_m': products_m,
    #             'form': form})



class IndexView(generic.ListView):
    # template = loader.get_template('products/index.html')
    # return HttpResponse("Hello, You are in <strong>product</strong> index")

    # Version 2
    # latest_product_list = Product.objects.order_by('-productPublish')[:5:-1]
    # context = {'latest_product_list': latest_product_list,}
    # return render(request, 'products/index.html', context)

    template_name = 'products/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:5:-1]


def prdimage(request, product_id):
    response = "You're looking at the images of product {}s."
    return HttpResponse(response.format(product_id))


class blog(generic.ListView):
    template_name = 'products/blog.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:5:-1]
