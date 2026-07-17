from django.urls import path
from .views import CoursesViewSet

urlpatterns = [
    path('courses/',CoursesViewSet.as_view({'get': 'list','post': 'create',}),),
    path('cours/<int:pk>/',CoursesViewSet.as_view({'get': 'retrieve','put': 'update','patch': 'partial_update','delete': 'destroy',}),),
]
