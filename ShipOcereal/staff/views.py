from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from home.models import Cereal, cerealImage
from user.models import SearchHistory
from staff.forms.cereal_form import CerealCreateForm, CerealUpdateForm
from staff.forms.image_form import imageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "admin/admin_home.html")

def customerView(request):
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
    return render(request, "admin/allProducts.html", context)



def get_cereal_by_id(request, id):
    return render(request, 'admin/admin_cereal_details.html', {
        'cereal': get_object_or_404(Cereal, pk=id)
    })

def create_images(cerealImage, Cereal):
    for img in cerealImage:
        if img != '':
            image = cerealImage(image='Placeholder', path=img)
            image.save()
            Cereal.image.add(image)



def create_cereal2(request):
    if request.method == 'POST':
        form = CerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            return redirect("staff-index")
    else:
        form = CerealCreateForm()
    return render(request, 'admin/create_cereal.html', {
        'form': form
    })

def create_cereal_start(request):
    if request.method == 'POST':
        form = imageForm(data=request.POST)
        if form.is_valid():
            image = form.save()
            return redirect('create_cereal2')
    else:
        form = imageForm()
    return render(request, 'admin/createCerealImage.html', {'form':form})


def delete_cereal(request, id):
    cereal = get_object_or_404(Cereal, pk=id)
    cereal.delete()
    return redirect('staff-index')

def update_cereal(request, id):
    instance = get_object_or_404(Cereal, pk=id)
    if request.method == 'POST':
        form = CerealUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('admin-cereal-details', id=id)
    else:
        form = CerealUpdateForm(instance=instance)
    return render(request, 'admin/update_cereal.html', {
        'form': form,
        'id': id
    })

def get_product_list(request):
    context = {'cereals' : Cereal.objects.all()}
    return render(request, "admin/product_list.html",context)
