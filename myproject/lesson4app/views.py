from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Good
from .forms import GoodForm


def good_edit(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES, instance=good)
        if form.is_valid():
            form.save()

    else:
        form = GoodForm(initial={
            'name': good.name,
            'description': good.description,
            'price': good.price,
            'quantity': good.quantity,
            'image': good.image
        })
    return render(request, "lesson4app/good.html", {'form': form, 'good': good})
