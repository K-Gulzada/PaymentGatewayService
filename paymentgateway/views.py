from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from paymentgateway.models import PaymentMethod, Transaction, Bank, Balance, PaymentStatus
from paymentgateway.serializers import PaymentMethodSerializer, TransactionSerializer, BankSerializer, \
    PaymentStatusSerializer, BalanceSerializer


@permission_classes((permissions.AllowAny,))
class PaymentMethodViews(APIView):

    def get(self, request):
        paymentMethods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(instance=paymentMethods, many=True)
        return JsonResponse({"paymentMethods": serializer.data})

    # {
    #     "PaymentMethod":{
    #     "methodName":"updatedName_2"
    #     }
    # }

    def post(self, request):
        paymentMethodData = request.data.get('PaymentMethod')
        serializer = PaymentMethodSerializer(data=paymentMethodData)
        if serializer.is_valid(raise_exception=True):
            paymentMethod = serializer.save()
        return JsonResponse(model_to_dict(paymentMethod))

    #
    def put(self, request, pk):
        saved_payment_method = get_object_or_404(PaymentMethod.objects.all(), pk=pk)
        data = request.data.get('PaymentMethod')
        serializer = PaymentMethodSerializer(instance=saved_payment_method, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_payment_method = serializer.save()
        return JsonResponse(model_to_dict(saved_payment_method))

    #
    def delete(self, request, pk):
        # Get object with this pk
        paymentMethod = get_object_or_404(PaymentMethod.objects.all(), pk=pk)
        paymentMethod.delete()
        return JsonResponse({
            "message": "Payment Method with id {} has been deleted.".format(pk)
        }, status=204)


@permission_classes((permissions.AllowAny,))
class BankViews(APIView):

    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(instance=banks, many=True)
        return JsonResponse({"banks": serializer.data})

    # {
    #     "Bank":{
    #     "config":"Bank 1 config_1"
    #     }
    # }

    def post(self, request):
        bankData = request.data.get('Bank')
        serializer = BankSerializer(data=bankData)
        if serializer.is_valid(raise_exception=True):
            bank = serializer.save()
        return JsonResponse(model_to_dict(bank))

    #
    def put(self, request, pk):
        saved_bank = get_object_or_404(Bank.objects.all(), pk=pk)
        data = request.data.get('Bank')
        serializer = BankSerializer(instance=saved_bank, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_bank = serializer.save()
        return JsonResponse(model_to_dict(saved_bank))

    #
    def delete(self, request, pk):
        # Get object with this pk
        bank = get_object_or_404(Bank.objects.all(), pk=pk)
        bank.delete()
        return JsonResponse({
            "message": "Bank with id {} has been deleted.".format(pk)
        }, status=204)


@permission_classes((permissions.AllowAny,))
class BalanceViews(APIView):

    def get(self, request):
        balances = Balance.objects.all()
        serializer = BalanceSerializer(instance=balances, many=True)
        return JsonResponse({"balances": serializer.data})

    # {
    #     "Balance":{
    #     "userId":1,
    #     "currentBalance": 980550.0,
    #     "date": "10-11-2020"
    #     }
    # }

    def post(self, request):
        balanceData = request.data.get('Balance')
        serializer = BalanceSerializer(data=balanceData)
        if serializer.is_valid(raise_exception=True):
            balance = serializer.save()
        return JsonResponse(model_to_dict(balance))

    #
    def put(self, request, pk):
        saved_balance = get_object_or_404(Balance.objects.all(), pk=pk)
        data = request.data.get('Balance')
        serializer = BalanceSerializer(instance=saved_balance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_balance = serializer.save()
        return JsonResponse(model_to_dict(saved_balance))

    #
    def delete(self, request, pk):
        # Get object with this pk
        balance = get_object_or_404(Balance.objects.all(), pk=pk)
        balance.delete()
        return JsonResponse({
            "message": "Balance with id {} has been deleted.".format(pk)
        }, status=204)


@permission_classes((permissions.AllowAny,))
class PaymentStatusViews(APIView):

    def get(self, request):
        paymentStatusList = PaymentStatus.objects.all()
        serializer = PaymentStatusSerializer(instance=paymentStatusList, many=True)
        return JsonResponse({"paymentStatusList": serializer.data})
    #
    # {
    #     "PaymentStatus":{
    #     "statusCode":404,
    #     "description": "Not Found"
    #     }
    # }

    def post(self, request):
        paymentStatusData = request.data.get('PaymentStatus')
        serializer = PaymentStatusSerializer(data=paymentStatusData)
        if serializer.is_valid(raise_exception=True):
            paymentStatus = serializer.save()
        return JsonResponse(model_to_dict(paymentStatus))

    #
    def put(self, request, pk):
        saved_payment_status = get_object_or_404(PaymentStatus.objects.all(), pk=pk)
        data = request.data.get('PaymentStatus')
        serializer = PaymentStatusSerializer(instance=saved_payment_status, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_payment_status = serializer.save()
        return JsonResponse(model_to_dict(saved_payment_status))

    #
    def delete(self, request, pk):
        # Get object with this pk
        balance = get_object_or_404(Balance.objects.all(), pk=pk)
        balance.delete()
        return JsonResponse({
            "message": "Balance with id {} has been deleted.".format(pk)
        }, status=204)


@permission_classes((permissions.AllowAny,))
class TransactionViews(APIView):

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(instance=transactions, many=True)
        return JsonResponse({"transactions": serializer.data})

    # {
    #     "Transaction":{
    #     "orderInfo":"Order 1 INFO",
    #     "sum": 54990,
    #     "statusId":1,
    #     "paymentMethodId":1,
    #     "BankId":1,
    #     "date":"27-12-2021"
    #     }
    # }

    def post(self, request):
        transactionData = request.data.get('Transaction')
        serializer = TransactionSerializer(data=transactionData)
        if serializer.is_valid(raise_exception=True):
            transaction = serializer.save()
        return JsonResponse(model_to_dict(transaction))

    #
    def put(self, request, pk):
        saved_transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        data = request.data.get('Transaction')
        serializer = TransactionSerializer(instance=saved_transaction, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_transaction = serializer.save()
        return JsonResponse(model_to_dict(saved_transaction))

    #
    def delete(self, request, pk):
        # Get object with this pk
        transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        transaction.delete()
        return JsonResponse({
            "message": "Transaction with id {} has been deleted.".format(pk)
        }, status=204)

#     search by userid
#  удалить префиксы
