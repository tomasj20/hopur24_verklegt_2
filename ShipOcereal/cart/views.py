from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.models import user_info, SearchHistory
from home.models import Cart, CartProduct
from user.models import user_info
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def index(request):
    user = request.user
    userInfo = user_info.objects.filter(user=user).first()
    cart = Cart.objects.filter(user=user).first()
    print(cart.id)
    cartItems = CartProduct.objects.filter(cart_id=cart.id)

    context = {'user':userInfo,'cartContent':cartItems}
    return render(request, "cart/cart.html",context)
