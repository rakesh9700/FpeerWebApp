from django.shortcuts import render

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

from django.core.files.storage import FileSystemStorage
from django.conf import settings

#def simple_upload(request):
 #   if request.method == 'POST' and request.FILES['myfile']:
  #      myfile = request.FILES['myfile']
   #     fs = FileSystemStorage()
    #    filename = fs.save(myfile.name, myfile)
     #   uploaded_file_url = fs.url(filename)
      #  return render(request, 'upload.html', {
       #     'uploaded_file_url': uploaded_file_url
        #})
    #return render(request, 'upload.html')

from .forms import DocumentForm
from django.shortcuts import redirect
import json

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home1')
    else:
        form = DocumentForm()
    return render(request,'upload.html', {
        'form': form
    })
