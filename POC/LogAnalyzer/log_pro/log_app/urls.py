from django.urls import path
from log_app import views
app_name = "log_app"

urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('analyze_log',views.AzlogView.as_view(),name="azlog"),
    path('analyze_site',views.AzsiteView.as_view(),name="azsite"),
]
