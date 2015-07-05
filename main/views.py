from django.shortcuts import render
from datetime import datetime

def local_item(request):
    local_item = 'local item'
    time = datetime.now()
    context = {
        'local_item': local_item,
        'time': time,
    }

    return render(
        request,
        'main/local.html',
        context,
    )

def global_item(request):
    time = datetime.now()
    context = {
        'time': time,
    }
    return render(
        request,
        'main/global.html',
        context
    )
