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
    path('<int:pk>/images/', views.prdimage, name='prdimage'),

]
