from django.shortcuts import render
from .models import FileUpload
from server.settings import BASE_DIR
from django.core.files.uploadedfile import InMemoryUploadedFile


def index(request):
    if request.method == 'POST':
        try:
            obj = FileUpload()
            obj.file = request.FILES['myfile']
            obj.save()
        except BaseException as e:
            print(e)
    return render(request, 'index.html', {'files':FileUpload.objects.all()})


def handle_uploaded_file(f:InMemoryUploadedFile):
    with open(BASE_DIR/'media'/f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)