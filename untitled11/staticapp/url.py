from django.conf.urls import include
from django.urls import path
from staticapp.views import base_view, category_view, product_view
from staticapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views
from . import models
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', base_view, name='base'),
    path('category/<str:category_slug>/', category_view, name ='category_detail'),
    path('product/<str:product_slug>/', product_view, name ='product_detail'),
    #path('category/', category_view, name ='category_detail'),
    #path('product/', product_view, name ='product_detail'),
    # path('cart1/',views.CartView.as_view(),name='')
    path('cartf/',views.get_cart,name='get_cart'),
    path('cartdel/<str:product_slug>/',views.clear,name='clear',),
    path('add_to_cart/<str:product_slug>/',views.add_to_cart,name='add_to_cart'),
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',views.RegisterFormView.as_view(),name='signup'),
    path('404/',views.error,name='error'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
