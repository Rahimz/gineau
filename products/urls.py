from django.urls import path
from . import views


# this specifies that 'detail' in products are different with
# detail in the other app
app_name = 'products'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.HomeView, name='home'),
    path('women/', views.WomenProductListView, name='womenproductlistview'),
    path('men/', views.MenProductListView, name='menproductlistview'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  
    path('<int:product_id>/images/', views.prdimage, name='prdimage'),
	path('blog/', views.blog.as_view(), name='blog'),
]
