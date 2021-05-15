from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.models import user_info, SearchHistory
from home.models import Cart, CartProduct, paymentInfo
from user.models import user_info
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.forms.paymentForm import PaymentForm

def index(request):
    user = request.user
    userInfo = user_info.objects.filter(user=user.id).first()
    print(user.id)
    cart = Cart.objects.filter(user_id=user.id).first()
    if cart == None:
        cart = Cart.objects.filter(userInfo_id=userInfo.id).first()
    cartItems = CartProduct.objects.filter(cart_id=cart.id)
    total = 0
    for item in cartItems:
        total += item.prod_price


    context = {'user':userInfo, 'cartContent':cartItems, 'total':total}
    return render(request, "cart/cart.html", context)


def paymentStep1(request):
    userData = user_info.objects.filter(user=request.user).first()
    print(userData.full_name)
    if request.method == 'POST':
        form = ProfileForm(instance=userData,data=request.POST)
        if form.is_valid():
            userData = form.save(commit=False)
            userData.user = request.user
            userData.save()
            return redirect('paymentstep2')
    return render(request, 'cart/paymentstep1.html', {
        'form':ProfileForm(instance=userData)
    })

def paymentStep2(request):
    userData = paymentInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentForm(instance=userData,data=request.POST)
        if form.is_valid():
            userData = form.save(commit=False)
            userData.user = request.user
            userData.save()
            return redirect('paymentstep3')
    return render(request,'cart/paymentstep2.html',{
        'form': PaymentForm(instance=userData)
    })

def paymentStep3(request):
    user = request.user
    userInfo = user_info.objects.filter(user=user.id).first()
    paymentinfo = paymentInfo.objects.filter(user=request.user).first()
    cart = paymentInfo.objects.filter(user=request.user).first()
    if cart == None:
        cart = Cart.objects.filter(userInfo_id=userInfo.id).first()
    cartitems = CartProduct.objects.filter(cart_id=cart.id)
    total = 0
    for item in cartitems:
        total += item.prod_price

    context = {'user':userInfo, 'payment':paymentinfo, 'cart':cart, 'cartitems': cartitems, 'total': total}
    return render(request, "cart/paymentstep3.html", context)

