from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('schedules/<int:id>',views.schedules, name='schedules' ),
    path('farmers/<int:id>', views.farmers, name = 'farmers'),
    # path('<char:crop>', views.crops, name='crops'),
    path('<int:id>', views.fertilisers, name='fertlisers'),


]