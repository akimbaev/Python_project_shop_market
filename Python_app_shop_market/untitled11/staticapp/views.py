from django.shortcuts import render
from staticapp.models import Category, Products
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from cart.cart import Cart
from django.shortcuts import render_to_response
# Create your views here.
def error(request):
    return render(request,'404.html')



def add_to_cart(request, product_slug):
    quantity=1
    product = Products.objects.get(slug = product_slug)
    cart = Cart(request)
    cart.add(product, product.price, quantity)

    return render_to_response('cart.html', dict(cart=Cart(request)))
def clear(request,product_slug):
    product = Products.objects.get(slug = product_slug)
    cart = Cart(request)
    cart.remove(product)
    return render_to_response('cart.html', dict(cart=Cart(request)))


def remove_from_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    print(dict(cart=Cart(request)))
    return render_to_response('cart.html', dict(cart=Cart(request)))

def base_view(request):
    categories = Category.objects.all()
    products = Products.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context)
def product_view(request,product_slug):
    product = Products.objects.get(slug = product_slug)
    #product = Products.objects.all()
    context ={
        'product': product
    }
    return render(request, 'product.html', context)
def category_view(request,category_slug):
    category = Category.objects.get(slug = category_slug)
    products_of_category = category.products_set.all()
    context ={
        'category': category,
        'products_of_category': products_of_category
    }
    return render(request, 'category.html', context)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "index.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "index.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
