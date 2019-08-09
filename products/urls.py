from django.urls import path
from . import views


# this specifies that 'detail' in products are different with
# detail in the other app
app_name = 'products'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('products/<int:pk>/', views.DetailView, name='detail'),
    path('products/<str:genre>/', views.ProductListView, name='productlistview'),
    path('tag/<slug:tag_slug>/', views.ProductListView, name='product_list_by_tag'),
    # path('user/email/', views.add_new_email, name='email_add'),
  
    path('blog/', views.blog.as_view(), name='blog'),
]
