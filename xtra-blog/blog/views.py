from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

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
        'page': 'index',
    }
    return render(request, 'index.html', context=context)


def about_page(request: HttpRequest) -> HttpResponse:
    context = {
        'page': 'about',
    }
    return render(request, 'about.html', context=context)


def contact_page(request: HttpRequest) -> HttpResponse:
    context = {
        'page': 'contact',
    }

    if request.method == 'GET':
        return render(request, 'contact.html', context=context)

    if request.method == 'POST':
        print(request.POST)

        with open('blog/contact_result.txt', 'a') as file:
            file.writelines(
                f"Name: {request.POST.get('name')}, "
                f"Email: {request.POST.get('email')}, "
                f"Subject: {request.POST.get('subject')}, "
                f"Message: {request.POST.get('message')}\n"
            )
        return redirect(contact_page)
