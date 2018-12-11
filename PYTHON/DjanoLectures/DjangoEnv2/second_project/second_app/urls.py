from django.urls import path,include
from second_app import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('help/',views.help_fn,name = "help_fn"),
]
