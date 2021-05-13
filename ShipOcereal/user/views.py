from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.models import user_info
from user.forms.profile_form import ProfileForm

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': UserCreationForm}
    return render(request, "user/register/placeholder.html", context)

def profile(request):
    userData = user_info.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=userData, data=request.POST)
        if form.is_valid():
            userData = form.save(commit=False)
            userData.user = request.user
            userData.save()
            return redirect('profileinfo')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=userData)
    })

def profile_info(request):
    return render(request, "user/profile_info.html",
                  context={"profile_info": user_info.objects.filter(user=request.user.id).first()})

