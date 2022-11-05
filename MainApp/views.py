from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    return render(request, 'index.html')


# /item/4
# /item/10
def get_item(request, id):
    try:
        item = Item.objects.get(pk=id)
        context = {
            "item": item
        }
        return render(request, 'item_page.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={id} not found")


def all_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items.html', context)
