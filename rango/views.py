from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Construct a dictinoary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to the client.
    # We make use of that shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context = context_dict)

#def about(request):
#    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

def about(request):
    context_dict = {'your_name': "James", 'name': "James"}
    return render(request, 'rango/about.html', context=context_dict)

#How to avoid duplication of context_dict above. Hmm!