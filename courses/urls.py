from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

urlpatterns = [
    path('courses/',views.courses_listview),
    path('courses/create/',views.courses_create),
    path('courses/<int:pk>/',views.courses_detail),
    path('courses/<int:pk>/update/',views.courses_update),
    path('courses/<int:pk>/delete/',views.courses_delete),
    path('courses/<int:pk>/patch/',views.courses_patch)

]



    

