from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item


# Create your views here.
def main(request):
    return render(request, 'index.html', {"page_title": "Home"})


def item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        "item": item,
        "page_title": f"Item:{item.name}",
        "page": "Item"
    }
    return render(request, 'item.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items,
        "page_title": "Items"
    }
    return render(request, 'items_list.html', context)
