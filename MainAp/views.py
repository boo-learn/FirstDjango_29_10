from django.shortcuts import render, HttpResponse

author = {
    "name": "Евгений",
    "surname": "Юрченко"
}


def main(request):
    return HttpResponse("Main page")


def about(request):
    text = f"{author['name']} {author['surname']}"
    return HttpResponse(text)
