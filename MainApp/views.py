from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item

author = {
    "name": "Евгений",
    "surname": "Юрченко",
    "midlename": "Витальевич",
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
    {"id": 6, "name": "Попкорн", "quantity": 4},
]


def main(request):
    return render(request, 'index.html')


def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Отчество: <b>{author['midlename']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    """
    return HttpResponse(text)


# /item/4
# /item/10
def get_item(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, 'item_page.html', context)
    return HttpResponseNotFound(f"Item with id={id} not found")


def all_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items.html', context)
