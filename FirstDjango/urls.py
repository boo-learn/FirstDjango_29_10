from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('about', views.about),
    path('item/<int:id>', views.get_item),
    path('items', views.all_items),
]
