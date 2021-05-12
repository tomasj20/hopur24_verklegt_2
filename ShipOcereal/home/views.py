from django.shortcuts import render, get_object_or_404
from home.models import Cereal
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
    return render(request, 'home/cereal_details.html', {
        'cereal': get_object_or_404(Cereal, pk=id)
    })