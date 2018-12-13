from django.conf.urls import url
from auth_app import views

#TEMPLATE URLS!

app_name = "auth_app"

urlpatterns = [
    url("register/",views.register,name="register"),
    url("user_login1/",views.user_login1,name="user_login2"),
]
