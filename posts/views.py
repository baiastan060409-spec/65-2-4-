from django.http import HttpResponse
from .models import Category

def category_list(request):
    categories = Category.objects.filter(is_active=True)

    result = ""

    for category in categories:
        result += f"{category.title} - {category.description}<br>"

    return HttpResponse(result)