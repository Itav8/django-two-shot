from django.urls import path
from receipts.views import create_receipt, list_account, list_expense_category, show_receipt


urlpatterns = [
    path("", show_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", list_expense_category, name="category_list"),
    path("accounts/", list_account, name="account_list"),
]
