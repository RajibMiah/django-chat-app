from django.shortcuts import render
import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def chatpage(request):
    return render(request, 'chat/chat/chatpage.html', {        
        'username': mark_safe(json.dumps(request.user.username)),
        'userid': mark_safe(json.dumps(request.user.id)),
        'domain':mark_safe(json.dumps(get_current_site(request).domain))
    })  


def logout_view(request):
    logout(request)
    return redirect('/admin/')
