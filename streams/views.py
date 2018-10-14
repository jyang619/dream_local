from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def stream(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'video.html', {'user': username})


    