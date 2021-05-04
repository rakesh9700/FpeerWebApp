# accounts/urls.py
from django.urls import path

from .views import SignUpView, model_form_upload#,simple_upload


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('upload/', model_form_upload , name = 'upload')
]