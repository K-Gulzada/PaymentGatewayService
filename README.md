В проекте PaymentGateService есть 5 классов (PaymentMethod, Bank, Balance, PaymentStatus, Transaction) и для каждого реализованы CRUD методы.

PaymentMethod
для получение PaymentMethod (getAll) нужно перейти по ссылке http://127.0.0.1:8000/payment-methods/, GET запрос.

       "PaymentMethod":{
       "methodName":"updatedName_2"
       }
Чтобы добавить PaymentMethod нужно перейти по той же ссылке только через POST запрос.
Для обновления и удаления PaymentMethod нужно перейти по ссылке http://localhost:8000/payment-methods/{id}. {id} это айди объекта, которого мы хотим обновить или удалить.

Bank
для получения выбора метода достаточно перейти по get ссылке http://127.0.0.1:8000/api/Bank

      "Bank":{
          "config":"Bank 1 config_1"
       }
 

примечание ( для изменение или удаление PaymentMethod или Bank переходем по put or delete (в зависемостри от сетуации)ссылке http://127.0.0.1:8000/api/PaymentMethod or Bank 
и через "/" пишем айди PaymentMethod или Bank которого хотели бы изменить или удалить )

Balance
для ввода данных сообщений переходим на -> post http://127.0.0.1:8000/api/Balance/ который ждет :

       "Balance":{
          "userId":1,
          "currentBalance": 980550.0,
          "date": "10-11-2020"
        }

