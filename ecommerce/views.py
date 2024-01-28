from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Create your views here.
def ecommerce_index_view(request):
    '''This function renders the index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742222 Intouch Sorn-in views!')

def Homepage(request):
    
    return HttpResponse('Homepage')

def Categorypage(request):
    return HttpResponse('Categorypage')

def Productpage(request):
    return HttpResponse('Productpage')

def Checkoutpage(request):
    return HttpResponse('Checkoutpage')

def Contactpage(request):
    return HttpResponse('Contactpage')


def item_view(request, item_id):
    context_data = {
        "item_id": item_id
        }
    return render(request, 'index.html', context=context_data)