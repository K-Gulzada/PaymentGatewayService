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
    "userId":4,
    "currentBalance":66000,
    "date":"2021-09-15"
    
}

Для обновления (PUT запрос) и удаления (DELETE запрос) Balance нужно перейти по ссылкам http://localhost:8000/updateBalance/{id} и http://localhost:8000/deleteBalance/{id} соответственно. {id} это айди объекта, которого мы хотим обновить или удалить.


     

