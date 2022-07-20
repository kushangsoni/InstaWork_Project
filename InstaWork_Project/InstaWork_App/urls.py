from django.urls import path
from .views import (
            UserListView,
            )
from . import views

urlpatterns = [
    path('',UserListView.as_view(),name='InstaWork_App-home'),
    path('user/new/', views.add, name='InstaWork_App-create'),
    path('user/edit/<int:id>', views.edit, name='InstaWork_App-edit'),
]
