В проекте PaymentGateService есть 5 классов (PaymentMethod, Bank, Balance, PaymentStatus, Transaction) и для каждого реализованы CRUD методы.

# PaymentMethod
для получение PaymentMethod (getAll) нужно перейти по ссылке http://127.0.0.1:8000/payment-methods/, GET запрос.

       "PaymentMethod":{
       "methodName":"updatedName_2"
       }
Чтобы добавить PaymentMethod нужно перейти по той же ссылке, только через POST запрос.
Для обновления и удаления PaymentMethod нужно перейти по ссылке http://localhost:8000/payment-methods/{id}. Это PUT и DELETE запросы соответственно. {id} это айди объекта, которого мы хотим обновить или удалить.

# Bank
для получения Bank (getAll)  достаточно перейти по ссылке http://127.0.0.1:8000/bank, GET запрос.

      "Bank":{
          "config":"Bank 1 config_1"
       }
 
Чтобы добавить Bank нужно перейти по той же ссылке, только через POST запрос.
Для обновления и удаления Bank нужно перейти по ссылке http://localhost:8000/bank/{id}. Это PUT и DELETE запросы соответственно. {id} это айди объекта, которого мы хотим обновить или удалить.


# Balance
для получения Balance (getAll) нужно перейти по ссылке http://127.0.0.1:8000/balance, GET запрос.

        "Balance":{
          "userId":1,
          "currentBalance": 980550.0,
          "date": "10-11-2020"
        }
 
Чтобы добавить Balance нужно перейти по ссылке http://localhost:8000/addNewBalance/, POST запрос. Пример body для добавления указан ниже:

       {
           "userId":4, <br/>
           "currentBalance":66000, <br/>
           "date":"2021-09-15" <br/>
       }

Для обновления (PUT запрос) и удаления (DELETE запрос) Balance нужно перейти по ссылкам http://localhost:8000/updateBalance/{id} и http://localhost:8000/deleteBalance/{id} соответственно. {id} это айди объекта, которого мы хотим обновить или удалить.

# Payment Status 
для получения PaymentStatus (getAll) нужно перейти по ссылке http://127.0.0.1:8000/payment-status/, GET запрос.
       "PaymentStatus":{
          "statusCode":403,
          "description": "Forbidden"
        }
 
Чтобы добавить PaymentStatus нужно перейти по той же ссылке, только через POST запрос. Пример body для добавления указан ниже:

       {
           "statusCode":404, <br/>
           "description": "Not Found" <br/>
       }

Для обновления (PUT запрос) и удаления (DELETE запрос) PaymentStatus нужно перейти по ссылке http://localhost:8000/payment-status/{statusCode}. {id} это айди объекта, которого мы хотим обновить или удалить.

# Transaction
для получения Transaction (getAll) нужно перейти по ссылке http://127.0.0.1:8000/transaction/, GET запрос.
 
Чтобы добавить Transaction нужно перейти по той же ссылке, только через POST запрос. Пример body для добавления указан ниже:

        {
           "orderInfo":"Order 1 INFO", <br/>
           "sum": 54990, <br/>
           "statusId":1, <br/>
           "paymentMethodId":1, <br/>
           "BankId":1, <br/>
           "date":"2021-12-12" <br/>
       }

