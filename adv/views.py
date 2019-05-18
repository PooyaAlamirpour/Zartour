from django.shortcuts import render


def adv_form(request):
    template = "shomareha/insert.html"
    return render(request, template, locals())


def adv_item(request):
    template = "shomareha/adv_item.html"
    return render(request, template, locals())


def search(request):
    template = "shomareha/search.html"
    return render(request, template, locals())