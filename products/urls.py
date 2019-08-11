from django.urls import path
from . import views


# this specifies that 'detail' in products are different with
# detail in the other app
app_name = 'products'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('products/women/', views.WomenListView, name='womenlistview'),
    path('products/men/', views.MenListView, name='menlistview'),
    path('products/<slug:prd>/', views.DetailView, name='detail'),
    path('tag/<slug:tag_slug>/', views.ProductListView, name='product_list_by_tag'),
    # path('user/email/', views.add_new_email, name='email_add'),
  
    path('blog/', views.blog.as_view(), name='blog'),
]
