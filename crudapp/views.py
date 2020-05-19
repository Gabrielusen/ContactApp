from .forms import BookForm
from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse


def index(request):
    form = Book.objects.all()
    return render(request, 'crudapp/base.html', {'form': form})


def upload(request):
    upload = BookForm()
    if request.method == 'POST':
        upload = BookForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index' }}">reload</a>""")
    else:
        return render(request, 'crudapp/upload_form.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookForm(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'crudapp/upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExists:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
