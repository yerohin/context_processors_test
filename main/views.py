from django.shortcuts import render_to_response
from datetime import datetime

def local_item(request):
    local_item = 'local item'
    time = datetime.now()
    context = {
        'local_item': local_item,
        'time': time,
    }

    return render_to_response(
        'main/local.html',
        context,
    )

def global_item(request):
    time = datetime.now()
    context = {
        'time': time,
    }
    return render_to_response(
        'main/global.html',
        context
    )
