from django.shortcuts import render

from receipts.models import Receipt


# Create your views here.
# def show_receipt(request):
#     receipts = Receipt.objects.all()
#     context = {
#         "receipt_list": receipts,
#     }
#     return render(request, "receipts/receipt_list.html", context)


def show_receipt(request):
    receipts = Receipt.objects.all()
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/receipt_list.html", context)
