from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
