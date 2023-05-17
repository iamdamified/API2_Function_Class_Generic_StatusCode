from django.urls import path
from .views import api_home_page, api_detail_page, mobile_detail_page, mobile_home_page

urlpatterns = [
    path("", api_home_page.as_view(), name="home"),
    path("<int:id>/detail/", api_detail_page.as_view(), name="detail"),
    path("<int:id>/mobiledetail/", mobile_detail_page.as_view(), name="mobile_detail"),
    path("mobilehome/", mobile_home_page.as_view(), name="mobilehome")
]