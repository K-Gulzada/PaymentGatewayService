
from django.contrib import admin
from paymentgateway.models import PaymentMethod
from paymentgateway.views import PaymentMethodViews
from django.urls import path, include

from rest_framework import routers, serializers, viewsets


class PaymentMethodSerializer(serializers.ModelSerializer):
    methodName = serializers.CharField(max_length=100)

    class Meta:
        model = PaymentMethod
        fields = ('__all__')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

app_name = "paymentMethods"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('payment-methods/', PaymentMethodViews.as_view()),
]

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
