from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "article"

urlpatterns = [


    path('addarticle/',views.add,name= "add"),
    path("update/<int:id>",views.update,name = "update"),
    path("delete/<int:id>",views.delete,name ="delete"),
    path("article/<int:id>",views.article,name = "article")




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
