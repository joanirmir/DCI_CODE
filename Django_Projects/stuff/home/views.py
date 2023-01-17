from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    # Exercise: If the method is GET, send the following "You are Getting it!"
    # otherwise if the method is POST, send the following "You are posting"
    # Use the HttpResponse
    # You may need to use Postman
    if request.method == "GET":
        text = "You are Getting it!"
    elif request.method == "POST":
        text = "Not allowed to post data."
    return HttpResponse(text)