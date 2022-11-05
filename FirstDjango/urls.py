from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="home"),
    path('get_items', views.all_items, name="all-items"),
    path('item/<int:id>', views.get_item),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
