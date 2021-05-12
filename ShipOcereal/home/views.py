from django.shortcuts import render, get_object_or_404, redirect
from home.models import Cereal, cerealImage
from home.forms.cereal_form import CerealCreateForm
import datetime
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    context = {'Cereals': Cereal.objects.all().order_by('name')}
    return render(request, "home/test.html", context)

def get_cereal_by_id(request, id):
    return render(request, 'cereal_details.html', {
        'cereal': get_object_or_404(Cereal, pk=id)
    })

def create_images(cerealImage, Cereal):
    for img in cerealImage:
        if img != '':
            image = cerealImage(image='Placeholder', path=img)
            image.save()
            Cereal.image.add(image)

def create_cereal(request):
    if request.method == 'POST':
        form = CerealCreateForm(request.POST)
        if form.is_valid():
            cereal = form.save()
            cereal.initialize()
            cerealImage = dict(request.POST)['image']
            create_images(cerealImage, Cereal)
            cereal.save()
            return redirect('index')
    else:
        form = CerealCreateForm()
        #TODO: CREATE NEW INSTANCE CerealCreateForm()
    return render(request, 'home/create_cereal.html', {
        'form': form
    })

def delete_cereal(request, id):
    cereal = get_object_or_404(Cereal, pk=id)
    Cereal.delete()
    return redirect('index')
