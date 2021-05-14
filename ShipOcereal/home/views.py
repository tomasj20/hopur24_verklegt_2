from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from home.models import Cereal, cerealImage
from home.forms.cereal_form import CerealCreateForm, CerealUpdateForm
from home.forms.image_form import imageForm
from django.contrib.auth.decorators import login_required
from user.models import SearchHistory
import datetime
from django.http import HttpResponse
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
@login_required
def create_images(cerealImage, Cereal):
    for img in cerealImage:
        if img != '':
            image = cerealImage(image='Placeholder', path=img)
            image.save()
            Cereal.image.add(image)


@login_required
def create_cereal(request):
    if request.method == 'POST':
        form = CerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = CerealCreateForm()
    return render(request, 'home/create_cereal.html', {
        'form': form
    })
@login_required
def create_cereal_start(request):
    if request.method == 'POST':
        form = imageForm(data=request.POST)
        if form.is_valid():
            image = form.save()
            return redirect('http://127.0.0.1:8000/create_cereal2')
    else:
        form = imageForm()
    return render(request, 'home/createCerealImage.html',{'form':form})

@login_required
def delete_cereal(request, id):
    cereal = get_object_or_404(Cereal, pk=id)
    cereal.delete()
    return redirect('http://127.0.0.1:8000/')
@login_required
def update_cereal(request, id):
    instance = get_object_or_404(Cereal, pk=id)
    if request.method == 'POST':
        form = CerealUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cereal-details', id=id)

    else:
        form = CerealUpdateForm(instance=instance)
    return render(request, 'home/update_cereal.html', {
        'form': form,
        'id': id
    })
