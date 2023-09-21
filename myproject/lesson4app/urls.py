from django.urls import path
from . import views

urlpatterns = [
    path('good/<int:good_id>', views.good_edit, name='good'),
]
