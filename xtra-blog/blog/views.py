from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


posts = [
    {
        'Title': 'Simple and useful HTML layout',
        'Description': 'There is a clickable image with beautiful hover '
                       'effect and active title link for each post item. '
                       'Left side is a sticky menu bar. Right side is a '
                       'blog content that will scroll up and down.',
        'Category': 'Travel',
        'Date': 'June 24, 2020',
        'Author': 'by Admin Nat',
    }
]


def index_page(request: HttpRequest) -> HttpResponse:
    context = {
        'articles': posts,
    }
    return render(request, 'index.html', context=context)
