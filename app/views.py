from django.shortcuts import render, HttpResponseRedirect
from .forms import SubordinateForm

def index(request):
    return render(request, 'app/index.html')

def subordinate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubordinateForm(request.POST)
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponseRedirect("/test")

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'app/subordinate.html')

def king(request):
    return render(request, 'app/king.html')

def king_subordinates(request):
    return render(request, 'app/king_subordinates.html')

def answer(request):
    return render(request, 'app/answer.html')

def test(request):
    return render(request, 'app/test.html')