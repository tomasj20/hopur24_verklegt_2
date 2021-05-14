from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.models import user_info, SearchHistory
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
def profile_menu(request):
    return render(request, "user/profile_menu.html", context={"user": user_info.objects.filter(user=request.user.id).first()})

@login_required
def profile_info(request):
    return render(request, "user/profile_info.html",
                  context={"user": user_info.objects.filter(user=request.user.id).first()})

@login_required
def search_history(request):
    s = SearchHistory.objects.filter(user=request.user.id)
    return render(request, "user/search_history.html", {
        "search_history": s
    })

