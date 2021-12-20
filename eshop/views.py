from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def category_detail(request, id):
    return render(request, 'index.html', {})


def product_detail(request, id):
    return render(request, 'index.html', {})


def cart_detail(request):
    return render(request, 'index.html', {})


def order_detail(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'index.html', {})


def add_to_cart(request, id):
    return render(request, 'index.html', {})