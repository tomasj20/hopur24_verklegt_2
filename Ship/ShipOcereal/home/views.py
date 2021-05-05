from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    today = datetime.datetime.now().date()
    return render(request, "header.html",{"today":today})