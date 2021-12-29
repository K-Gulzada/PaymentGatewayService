from rest_framework import serializers

from paymentgateway.models import PaymentMethod, Transaction, Bank, Balance, PaymentStatus


class PaymentMethodSerializer(serializers.ModelSerializer):
    methodName = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return PaymentMethod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.methodName = validated_data.get('methodName', instance.methodName)
        instance.save()
        return instance

    class Meta:
        model = PaymentMethod
        fields = ('__all__')


class BankSerializer(serializers.ModelSerializer):
    config = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Bank.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.config = validated_data.get('config', instance.config)
        instance.save()
        return instance

    class Meta:
        model = Bank
        fields = ('__all__')


class BalanceSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField()
    currentBalance = serializers.DecimalField(max_digits=16, decimal_places=2)
    date = serializers.DateField(format="%d-%m-%Y")

    def create(self, validated_data):
        return Balance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.currentBalance = validated_data.get('currentBalance', instance.currentBalance)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance

    class Meta:
        model = Balance
        fields = ('__all__')


class PaymentStatusSerializer(serializers.ModelSerializer):
    statusCode = serializers.IntegerField()
    description = serializers.CharField()

    def create(self, validated_data):
        return PaymentStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.statusCode = validated_data.get('statusCode', instance.statusCode)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

    class Meta:
        model = PaymentStatus
        fields = ('__all__')


class TransactionSerializer(serializers.ModelSerializer):
    # orderInfo = serializers.CharField(max_length=255)
    # sum = serializers.IntegerField()
    # statusId = serializers.IntegerField()
    # paymentMethodId = serializers.IntegerField()
    # BankId = serializers.IntegerField()
    # date = serializers.DateField(format="%d-%m-%Y")
    #
    # def create(self, validated_data):
    #     return Transaction.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.orderInfo = validated_data.get('orderInfo', instance.orderInfo)
    #     instance.sum = validated_data.get('sum', instance.sum)
    #     instance.statusId = validated_data.get('statusId', instance.statusId)
    #     instance.paymentMethodId = validated_data.get('paymentMethodId', instance.paymentMethodId)
    #     instance.BankId = validated_data.get('BankId', instance.BankId)
    #     instance.date = validated_data.get('date', instance.date)
    #
    #     instance.save()
    #     return instance

    class Meta:
        model = Transaction
        fields = ('__all__')

    def to_representation(self, instance):
        self.fields['statusId'] = PaymentStatusSerializer(read_only=True)
        self.fields['paymentMethodId'] = PaymentMethodSerializer(read_only=True)
        self.fields['BankId'] = BankSerializer(read_only=True)
        return super(TransactionSerializer, self).to_representation(instance)

