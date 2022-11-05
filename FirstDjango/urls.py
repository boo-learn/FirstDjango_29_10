from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('items', views.all_items),
    path('item/<int:id>', views.get_item),
]
