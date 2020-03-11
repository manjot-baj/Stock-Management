from django.db.models import (Case, CharField, Count, DateTimeField,
                              ExpressionWrapper, F, FloatField, Func, Max, Min,
                              Prefetch, Q, Sum, Value, When, Subquery)
from SM import amc
from datetime import datetime
import http.client
import json

conn = http.client.HTTPSConnection("api.msg91.com")


def amcSms():
    today_amc = []
    data = list(amc.AMC.objects.all().values('pk', 'first_service_date', 'second_service_date',
                                             'third_service_date', 'fourth_service_date').annotate(
        amc_client=F('client_name__name'),
        amc_client_phone=F('client_name__phone'),
    ))

    for each in data:
        if each.get('first_service_date') == datetime.today().date() \
                or each.get('second_service_date') == datetime.today().date() \
                or each.get('third_service_date') == datetime.today().date() \
                or each.get('fourth_service_date') == datetime.today().date():
            client_no = each.get('amc_client_phone')
            client = each.get('amc_client')
            today_amc.append([client, client_no])
            payload = {
                "sender": "KIINFO",
                "route": "4",
                "country": "91",
                "sms": [
                    {
                        "message": f"Dear {client},\n Your AMC Service date is Today.\n"
                                   f"Our Technician will come today for Servicing.\n For more details call on "
                                   f"8080101993 / 9765957141\n Thanks and Regards,\n"
                                   f" Kalpesh Infotech\n"
                                   f"[www.kalpeshinfotech.com]",
                        "to": [
                            client_no,
                        ]
                    }
                ]
            }
            my_payload = json.dumps(payload)
            print(my_payload)
            headers = {
                'authkey': "319771ADVdNvaEDkN5e525394P1",
                'content-type': "application/json"
            }
            # conn.request("POST", "/api/v2/sendsms", my_payload, headers)
            # res = conn.getresponse()
            # data = res.read()
            # print(data.decode("utf-8"))
            amc.AMCRecord(date=datetime.today().date(), client=client, phone=client_no, message=f"Dear {client},\n "
                                                                                                f"Your AMC Service "
                                                                                                f"date is Today.\n "
                                                                                                f"Our Technician will "
                                                                                                f"come today for "
                                                                                                f"Servicing.\n For "
                                                                                                f"more details call on "
                                                                                                f"8080101993 / "
                                                                                                f"9765957141\n Thanks "
                                                                                                f"and Regards,\n "
                                                                                                f" Kalpesh Infotech\n"
                                                                                                f"[www"
                                                                                                f".kalpeshinfotech.com]"
                          ).save()
    if len(today_amc) == 0:
        return "today No AMC Service"
    return today_amc
