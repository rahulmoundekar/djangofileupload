from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from fileupload.forms import DocumentForm
from fileupload.models import Document


def index(request):
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fs = FileSystemStorage()
        filename = fs.save(upload.name, upload)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'simple.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'form.html', {'form': form})
