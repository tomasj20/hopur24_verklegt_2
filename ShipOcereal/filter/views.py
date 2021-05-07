from django.shortcuts import render

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def healthyIndex(request):
    return render(request, "filter/healthy.html")

def sugaryIndex(request):
    return render(request, "filter/sugary.html")

def veganIndex(request):
    return render(request, "filter/vegan.html")
