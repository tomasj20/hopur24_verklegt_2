from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from home.models import Cereal, cerealImage, CartProduct, Cart
from django.contrib.auth.decorators import login_required
from user.models import SearchHistory, user_info
import datetime
from django.http import HttpResponse
import json
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        cereals = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image.path
        } for x in Cereal.objects.filter(name__icontains=search_filter)]
        if request.user.is_authenticated:
            s = SearchHistory(user=request.user, search= search_filter)
            s.save()
        return JsonResponse({'data': cereals})
    context = {'Cereals': Cereal.objects.all().order_by('name')}
    return render(request, "home/test.html", context)

@login_required
def get_cereal_by_id(request, id):
    return render(request, 'cereal_details.html', {
        'cereal': get_object_or_404(Cereal, pk=id)
    })
def updateItem(request):
    data = json.loads(request.body)
    cerealId = data['cerealId']
    action = data['action']
    print('Action', action)
    print('cerealId', cerealId)
    userData,created = user_info.objects.get_or_create(user=request.user)
    cereal = Cereal.objects.get(id=cerealId)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if created == True:
        print('cart for user',userData.user.username,'created')
    if created == False:
        print('Cart for user',userData.user.username,'fetched')
    cartProduct, created = CartProduct.objects.get_or_create(cart=cart,
                                                             product_id=cereal.id,
                                                             product_name=cereal.name,
                                                             prod_price=cereal.price,
                                                             quantity=0
                                                             )
    if action == "add":
        cartProduct.quantity = (cartProduct.quantity + 1)
    elif action == "remove":
        cartProduct.quantity = (cartProduct.quantity - 1)

    cartProduct.save()

    if CartProduct.quantity == 0:
        CartProduct.delete()

    return JsonResponse('Item was added', safe=False)


