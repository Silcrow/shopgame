from django.shortcuts import render

from shop.models import Merchandise


def shop(request):
    items = Merchandise.objects.all()
    return render(request, 'shop/shop.html', {'items': items})
