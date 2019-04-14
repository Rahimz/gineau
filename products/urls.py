from django.urls import path
from . import views


# this specifies that 'detail' in products are different with
# detail in the other app
app_name = 'products'
urlpatterns = [
    # /products/
    path('', views.IndexView.as_view(), name='index'),
    # /products/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /products/1/images/
    path('<int:product_id>/images/', views.prdimage, name='prdimage'),
	path('blog/', views.blog.as_view(), name='blog'),
    # path('ui/template/', views.UIView, name='uiview'),
    path('ui/', views.UIHomeView, name='uihome'),
    path('ui/products/', views.UIProductListView, name='uiproductlistview'),

]
