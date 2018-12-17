from django.urls import path
from cbv_app import views

app_name = "cbv_app"

urlpatterns = [
    path('index1/',views.IndexView.as_view(),name = "index"),
    path('list1/',views.SchoolListView.as_view(),name = "list"),
    path('list1/<int:pk>/',views.SchoolDetailView.as_view(),name = "detail"),
    path('schools_detail/',views.SchoolInfoView,name = "sdetail"),
]
