from django.urls import path
from relurl_app import views

app_name = 'relurl_app'

urlpatterns=[
    path('relative/',views.relative,name = "relative"),
    path('other/',views.other,name = "other"),
]
