from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.main, name="home-page"),
    path('items/', views.items_list, name="items-list"),
    path('item/<int:id>/', views.item, name="item-page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
