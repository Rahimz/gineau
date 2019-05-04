from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Product
from django.template import loader

# Create your views here.


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


def prdimage(request, product_id):
    response = "You're looking at the images of product {}s."
    return HttpResponse(response.format(product_id))


class blog(generic.ListView):
    template_name = 'products/blog.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:5:-1]


def UIView(request):
    return render(request,
                  'products/new_base.html',
                  {})


class HomeView(generic.ListView):
    template_name = 'products/home.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-productPublish')[:5:-1]

    # return render(request,
    #               'products/home.html',
    #               {})

def ProductListView(request):
    return render(request,
                  'products/products_list.html',
                  {})
