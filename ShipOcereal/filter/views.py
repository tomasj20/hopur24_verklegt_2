from django.shortcuts import render

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def healthyIndex(request):
    return render(request, "healthy.html")
def sugaryIndex(request):
    return render(request, "sugary.html")
def veganIndex(request):
    return render(request, "vegan.html")
