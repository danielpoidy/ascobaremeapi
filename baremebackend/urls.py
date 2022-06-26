from django.contrib import admin
from django.urls import path
from souscripteurs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/souscripteurs', views.SouscripteursList.as_view())
]
