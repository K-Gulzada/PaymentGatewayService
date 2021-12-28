from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.utils import json
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
        # paymentMethodData = request.data.get('PaymentMethod')
        paymentMethodData = request.data
        serializer = PaymentMethodSerializer(data=paymentMethodData)
        if serializer.is_valid(raise_exception=True):
            paymentMethod = serializer.save()
        return JsonResponse(model_to_dict(paymentMethod))

    #
    def put(self, request, pk):
        saved_payment_method = get_object_or_404(PaymentMethod.objects.all(), pk=pk)
        # data = request.data.get('PaymentMethod')
        data = request.data
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
        # bankData = request.data.get('Bank')
        bankData = request.data
        serializer = BankSerializer(data=bankData)
        if serializer.is_valid(raise_exception=True):
            bank = serializer.save()
        return JsonResponse(model_to_dict(bank))

    #
    def put(self, request, pk):
        saved_bank = get_object_or_404(Bank.objects.all(), pk=pk)
        # data = request.data.get('Bank')
        data = request.data
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

    def get(self):
        balances = Balance.objects.all()
        serializer = BalanceSerializer(instance=balances, many=True)
        return JsonResponse({"balances": serializer.data})

    #     search by userid
    def getBalanceByUserId(self, pk):
        balance = Balance.objects.get(pk=pk)
        serializer = BalanceSerializer(instance=balance)
        return JsonResponse({"balance": serializer.data})

    # {
    #     "Balance":{
    #     "userId":1,
    #     "currentBalance": 980550.0,
    #     "date": "10-11-2020"
    #     }
    # }

    def post(self, request):
        # balanceData = request.data.get('Balance')
        balanceData = request.data
        serializer = BalanceSerializer(data=balanceData)
        if serializer.is_valid(raise_exception=True):
            balance = serializer.save()
        return JsonResponse(model_to_dict(balance))

    #
    def put(self, request, pk):
        saved_balance = get_object_or_404(Balance.objects.all(), pk=pk)
        # data = request.data.get('Balance')
        data = request.data
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
        # paymentStatusData = request.data.get('PaymentStatus')
        paymentStatusData = request.data
        serializer = PaymentStatusSerializer(data=paymentStatusData)
        if serializer.is_valid(raise_exception=True):
            paymentStatus = serializer.save()
        return JsonResponse(model_to_dict(paymentStatus))

    #
    def put(self, request, pk):
        saved_payment_status = get_object_or_404(PaymentStatus.objects.all(), pk=pk)
        # data = request.data.get('PaymentStatus')
        data = request.data
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
        # transactionData = request.data.get('Transaction')
        # transactionData = request.data
        # serializer = TransactionSerializer(data=transactionData)
        # if serializer.is_valid(raise_exception=True):
        #     transaction = serializer.save()
        # return JsonResponse(model_to_dict(transaction))

        # {
        #      "Transaction":{
        #     "orderInfo":"Order 1 INFO",
        #     "sum": 54990,
        #     "statusId":500,
        #     "paymentMethodId":1,
        #     "BankId":2,
        #     "date":"2021-12-12"
        #      }
        # }




        data = json.loads(request.body.decode('utf-8'))['Transaction']
        orderInfo = data['orderInfo']
        sumFromBody = data['sum']
        statusId = data['statusId']
        paymentMethodId = data['paymentMethodId']
        bankId = data['BankId']
        dateFromBody = data['date']

        paymentStatus = PaymentStatus.objects.get(statusCode=statusId)
        serializer_1 = PaymentStatusSerializer(instance=paymentStatus)
        paymentStatus = serializer_1.save()

        paymentMethod = PaymentMethod.objects.get(id=paymentMethodId)
        serializer_2 = PaymentMethodSerializer(instance=paymentMethod)
        paymentMethod = serializer_2.save()

        bank = Bank.objects.get(id=bankId)
        serializer_3 = BankSerializer(instance=bank)
        bank = serializer_3.save()

        transaction = Transaction(orderInfo=orderInfo, sum=sumFromBody, statusId=paymentStatus.statusCode,
                                  paymentMethodId=paymentMethod.id,
                                  BankId=bank.id, date=dateFromBody)

        # template = Template.objects.get(id=notification.templateID.id)
        #
        # text = template.text
        #
        # for i in params:
        #     text = text.replace('#' + i, params[i])
        #
        # if notification.sendMethodID.id == 1:
        #     email = EmailMessage(template.name, text, to=['sniper123zoom@gmail.com'])
        #     email.send()
        # elif notification.sendMethodID.id == 2:
        #     # https://telepot.readthedocs.io/en/latest/
        #     bot = telepot.Bot('5004111173:AAGrkTPki8mSDRQUpNgU30WlmSCA8bw_dd8')
        #     bot.sendMessage(861921150,
        #                     text)  # id key from chat https://api.telegram.org/bot5004111173:AAGrkTPki8mSDRQUpNgU30WlmSCA8bw_dd8/getUpdates
        #     # telegram_send.send(messages=["Wow that was easy!"])
        #
        # notification.save()
        # return JsonResponse(model_to_dict(notification))
        #
        # if serializer.is_valid(raise_exception=True):
        #     notification = serializer.save()
        #
        # id = notification.templateID
        # id = int(id.id)
        #
        # template = Template.objects.get(id=id).text
        # template = template.replace('#', notification.params)
        # email = EmailMessage(serializer.date, template, to=['sniper123zoom@gmail.com'])
        # email.send()

        return JsonResponse(model_to_dict(transaction))

    #
    def put(self, request, pk):
        saved_transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        # data = request.data.get('Transaction')
        data = request.data
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
