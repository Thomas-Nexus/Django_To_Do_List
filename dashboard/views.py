from django.shortcuts import render, redirect
from .models import *
from .forms import *

def todo(request):
    items = Item.objects.all()
    form = ItemsForm()
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'items': items, 'form': form}
    return render(request, 'todo.html', context)


def change(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemsForm(instance=item)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'item': item, 'form': form}
    return render(request, 'change.html', context)


def remove(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'remove.html', context)
