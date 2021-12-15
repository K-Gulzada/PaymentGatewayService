from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from paymentgateway.models import PaymentMethod

@permission_classes((permissions.AllowAny,))
class PaymentMethodViews(APIView):

    def get(self, request):
        paymentMethods = PaymentMethod.objects.all()
        return Response({"paymentMethods": paymentMethods})

    def post(self, request):
        # serializer = PaymentMethodSerializer(data=request.data)
        print(request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)