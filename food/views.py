from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import Item
from django.contrib.auth.decorators import login_required
from django.template import loader
from .forms import ItemForm
import traceback

# Create your views here.

@login_required
def index(request):
    template = loader.get_template('food/dummy.html')
    context = {}
    # return HttpResponse({"message":"Hello, There!"})
    return HttpResponse(template.render(context, request))

@login_required
def item(request):
    itemList = Item.objects.all()

    # template = loader.get_template('food/items.html')

    context = {
        'title': 'Items',
        'itemList' : itemList
    }

    return render(request, 'food/items.html', context)

@login_required
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


@login_required
def updateItem(request, itemId):
    item = Item.objects.get(pk=itemId)
    context = {
        'item': item,
    }

    if request.method == 'POST':
        # print(request.POST[""])
        name = request.POST["name"]
        price = float(request.POST["price"])
        description = request.POST['description']
        image = request.POST['image']


        item.name = name
        item.price = price
        item.description = description
        item.image = image
        item.save()

        return redirect('food:items')
    else:
        return render(request, 'food/update.html', context)


@login_required
def addItem(request):
    context = {
        'title' : "Add Item",
        'defaultUrl' : 'https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png'
    }


    if request.method == 'POST':
        name = request.POST['name'].title()
        price = float(request.POST['price'])
        description = request.POST['description']
        image = request.POST['image']

        newItem = Item()
        newItem.name = name
        newItem.price = price
        newItem.description = description
        newItem.image = image

        newItem.save()

        return redirect('food:items')
    else:
        return render(request, 'food/add.html', context)

@login_required
def deleteItem(request, itemId):
    item = Item.objects.get(pk=itemId)

    context = {
        'title' : f'Delete {item.name}',
        'item' : item
    }

    if request.method == 'POST':
        item.delete()

        return redirect('food:items')

    return render(request, 'food/delete.html', context)

@login_required
def add2(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        print('form valid')
        form.save()

        return redirect('food:items')


    return render(request, 'food/form.html', {'form': form, 'buttonName': 'Save'})

@login_required
def update2(request, itemId):
    item = Item.objects.get(pk=itemId)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        # print('Form submit')
        form.save()

        return redirect('food:items')

    return render(request, 'food/form.html', {'form':form, 'buttonName': 'Update'})

@login_required
def delete(request, itemId):
    item = Item.objects.get(pk=itemId)

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        item.delete()
        return redirect('food:items')


    return render(request, 'food/form.html', {'form': form, 'buttonName': 'Delete'})