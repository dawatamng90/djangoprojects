from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def greeting(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = '<h1>Hello friends. Good '
    
    if h < 12:
        msg += 'Morning!</h1>'
    elif h >= 12 and h < 16:
        msg += 'Afternoon!</h1>'
    elif h >= 16 and h < 21:
        msg += 'Evening!</h1>'
    else:
        msg += 'Night!</h1>'
    
    return HttpResponse(msg)
