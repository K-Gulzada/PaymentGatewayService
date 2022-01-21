
from django.contrib import admin
# from paymentgateway.views import PaymentMethodViews, TransactionViews, BankViews, PaymentStatusViews
from django.urls import path, include

from paymentgateway import views
from paymentgateway.views import PaymentMethodViews, TransactionViews, BankViews, BalanceViews, PaymentStatusViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

app_name = "paymentMethods"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),

    path('payment-methods/', PaymentMethodViews.as_view()),
    path('payment-methods/<int:pk>', PaymentMethodViews.as_view()),

    path('bank/', BankViews.as_view()),
    path('bank/<int:pk>', BankViews.as_view()),

    path('balance/', BalanceViews.get),
    path('balance/<int:pk>', BalanceViews.getBalanceByUserId),
    path('addNewBalance/', BalanceViews.as_view()),
    path('updateBalance/<int:pk>', BalanceViews.as_view()),
    path('deleteBalance/<int:pk>', BalanceViews.as_view()),

    path('payment-status/', PaymentStatusViews.as_view()),
    path('payment-status/<int:pk>', PaymentStatusViews.as_view()),

    path('transaction/', TransactionViews.as_view()),
    path('transaction/<int:pk>', TransactionViews.as_view()),
]

