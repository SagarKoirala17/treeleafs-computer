from django.urls import path
from .views import Homepage,Create,Update,Delete

urlpatterns=[
    path('',Homepage.as_view(),name='homepage'),
    path('create/',Create.as_view(),name='create'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('delete/<int:id>',Delete.as_view(),name='delete')
]