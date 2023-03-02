from django.urls import path
from receipts.views import create_receipt, show_receipt


urlpatterns = [
    path("", show_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt")
]
