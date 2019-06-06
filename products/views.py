from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Product
from django.template import loader


def HomeView(request):
    products_w = Product.objects.filter(productGenre="women")
    products_m = Product.objects.filter(productGenre="men")
    return render(request,
                  'products/new_base.html',
                  {'products_w': products_w,
                  'products_m': products_m,
                   })
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:8:-1]


def WomenProductListView(request):
    products = Product.objects.filter(productGenre="women")
    return render(request,
                  'products/products_list_w.html',
                  {'products': products,
                   'genre':'Women'})

def MenProductListView(request):
    products = Product.objects.filter(productGenre="men")
    return render(request,
                  'products/products_list_w.html',
                  {'products': products,
                   'genre':'Men'})


class DetailView(generic.DetailView):
    # try:
    #    product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #    raise Http404("Product does not exist")

    # version 2
    # product = get_object_or_404(Product, pk=product_id)
    # return render(request, 'products/detail.html', {'product':product})

    model = Product
    template_name = 'products/detail.html'


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
