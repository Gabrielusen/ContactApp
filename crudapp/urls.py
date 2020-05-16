from django.urls import path
from .views import IndexView, ContactDetailView, create, edit, delete


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>', edit, name='edit'),
    path('contacts/create', create, name='create'),
    path('contacts/delete/<int:pk>', delete, name='delete')
]
