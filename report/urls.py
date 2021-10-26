from django.urls import path
from .import views

urlpatterns=[
    path('create/field-report',views.DailyFieldReportsAPI.as_view(),name='create-report'),
    path('',views.index)

]