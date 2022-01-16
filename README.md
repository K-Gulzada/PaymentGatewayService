PaymentMethod
для получение шаблона нужно перейти по get ссылке http://127.0.0.1:8000/api/PaymentMethod

       "PaymentMethod":{
       "methodName":"updatedName_2"
       }
что бы добавить PaymentMethod нужно перейти по той же ссылке только через post

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

