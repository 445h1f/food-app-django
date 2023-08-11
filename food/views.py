from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('food/dummy.html')
    context = {}
    # return HttpResponse({"message":"Hello, There!"})
    return HttpResponse(template.render(context, request))


def item(request):
    itemList = Item.objects.all()

    # template = loader.get_template('food/items.html')

    context = {
        'title': 'Items',
        'itemList' : itemList
    }

    return render(request, 'food/items.html', context)


def details(request, itemId):
    try:
        item = Item.objects.get(pk=itemId)
        context = {
            'title': f'{item.name} Details',
            'item' : item
        }
        return render(request, 'food/details.html', context)
    except:
        return render(request, 'food/404.html')