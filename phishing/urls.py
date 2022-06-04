 
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
   #path('admin/', admin.site.urls),
   path('', views.button),
   path('index.html/', views.button),
  
   path('instagram/',views.runInsta),
   path('facebook/',views.runFacebook),
   path('paypal/',views.runPaypal),
   path('database.html/',views.database),
   path('delete.html/',views.deleteEntry),
   path('search.html/',views.search),


]
 

