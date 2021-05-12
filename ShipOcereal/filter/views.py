from django.shortcuts import render, get_object_or_404
from home.models import Cereal
from django.http import HttpResponse
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def healthyIndex(request):
    context = {'Cereals': Cereal.objects.filter(category_id=1).order_by('name')}
    return render(request, "filter/healthy.html",context)

def get_cereal_by_id(request, id):
    return render(request, 'cereal_details.html', {
        'cereal': get_object_or_404(Cereal, pk=id)
    })

def sugaryIndex(request):
    context = {'Cereals': Cereal.objects.filter(category_id=2).order_by('name')}
    return render(request, "filter/sugary.html",context)

def veganIndex(request):
    context = {'Cereals': Cereal.objects.filter(category_id=3).order_by('name')}
    return render(request, "filter/vegan.html",context)
