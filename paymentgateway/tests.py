import json

from django.test import TestCase
from rest_framework.generics import get_object_or_404

from paymentgateway.models import PaymentMethod


class PaymentMethodTest(TestCase):
    def test_getAllData(self):
        response = self.client.get("http://localhost:8000/payment-methods/")
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_postData(self):
        payment_for_test = {
            "methodName": "name_7"
        }
        response = self.client.post("http://localhost:8000/payment-methods/", json.dumps(payment_for_test),
                                    content_type="application/json")

        # print(get_object_or_404(PaymentMethod.objects.all(), pk=response.))
        print(json.loads(response.content))
        json_object = json.loads(response.content)

        print(json_object["id"])
        self.assertEqual(response.status_code, 200)
