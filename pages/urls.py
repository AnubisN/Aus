from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:message_id>', views.MessageFromCEO, name='messages'),
]
