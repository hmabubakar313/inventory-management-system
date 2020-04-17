from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .form import*
# Create your views here.


def index(request):
    return render(request, 'index.html')


def laptop(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops'
    }
    return render(request, 'index.html', context)


def desktop(request):
    items = Desktops.objects.all()
    context = {
        'items': items,
        'header': 'Desktop'
    }
    return render(request, 'index.html', context)


def mobile(request):
    items = Mobiles.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles'
    }
    return render(request, 'index.html', context)


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, "add_new.html", {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


def edit_device(request, pk, model, cls):
    item = get_object_or_404(Laptops, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def edit_laptop(request, pk):
    return edit_device(request, pk, Laptops, LaptopForm)


def edit_desktop(request, pk):
    return edit_device(request, pk, Desktops, DesktopForm)


def edit_mobile(request, pk):
    return edit_device(request, pk, Mobiles, MobileForm)
