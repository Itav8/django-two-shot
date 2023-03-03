from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from receipts.forms import AccountForm, CategoryForm, ReceiptForm
from receipts.models import Account, ExpenseCategory, Receipt


# Create your views here.
# def show_receipt(request):
#     receipts = Receipt.objects.all()
#     context = {
#         "receipt_list": receipts,
#     }
#     return render(request, "receipts/receipt_list.html", context)


@login_required(redirect_field_name="user_login")
def show_receipt(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/list_receipt.html", context)


@login_required(redirect_field_name="user_login")
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_receipt.html", context)


@login_required(redirect_field_name="user_login")
def list_expense_category(request):
    expense_categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expense_category_list": expense_categories,
    }
    return render(request, "receipts/list_category.html", context)


@login_required(redirect_field_name="user_login")
def list_account(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "account_list": accounts,
    }
    return render(request, "receipts/list_accounts.html", context)


@login_required(redirect_field_name="user_login")
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_category.html", context)


@login_required(redirect_field_name="user_login")
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_account.html", context)
