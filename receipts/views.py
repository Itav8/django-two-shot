from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm
from receipts.models import Receipt


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
    return render(request, "receipts/receipt_list.html", context)


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
