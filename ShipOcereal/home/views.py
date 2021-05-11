from django.shortcuts import render
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