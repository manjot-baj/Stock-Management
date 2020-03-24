from django.db.models import (Case, CharField, Count, DateTimeField,
                              ExpressionWrapper, F, FloatField, Func, Max, Min,
                              Prefetch, Q, Sum, Value, When, Subquery)
from SM import amc
from datetime import datetime, timedelta
import http.client
import json

conn = http.client.HTTPSConnection("api.msg91.com")


def amcSms():
    today_amc = []
    data = list(amc.AMC.objects.all().values('pk',
                                             'first_service_date',
                                             'second_service_date',
                                             'third_service_date',
                                             'fourth_service_date'
                                             ).annotate(
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
                                                                                                f".kalpeshinfotech.com]",
                          company_id=1).save()
    if len(today_amc) == 0:
        return "Today No AMC Service"
    return today_amc


def amcAlert(request):
    tommorrow_amc = []
    data = list(amc.AMC.objects.filter(company_id=request.session.get('company_id')).values(
        'pk', 'first_service_date', 'second_service_date', 'third_service_date', 'fourth_service_date').annotate(
        amc_client=F('client_name__name'),
        amc_client_phone=F('client_name__phone'),
    ))
    service_status = ""

    for each in data:
        if each.get('first_service_date') - timedelta(days=1) == datetime.today().date() \
                or each.get('second_service_date') - timedelta(days=1) == datetime.today().date() \
                or each.get('third_service_date') - timedelta(days=1) == datetime.today().date() \
                or each.get('fourth_service_date') - timedelta(days=1) == datetime.today().date():
            client_no = each.get('amc_client_phone')
            client = each.get('amc_client')
            if each.get('first_service_date') - timedelta(days=1) == datetime.today().date():
                service_status = "First Service"
                tommorrow_amc.append({"date": datetime.today().date() + timedelta(days=1), "client": client,
                                      'service_status': service_status, "phone": client_no})
            elif each.get('second_service_date') - timedelta(days=1) == datetime.today().date():
                service_status = "Second Service"
                tommorrow_amc.append({"date": datetime.today().date() + timedelta(days=1), "client": client,
                                      'service_status': service_status, "phone": client_no})
            elif each.get('third_service_date') - timedelta(days=1) == datetime.today().date():
                service_status = "Third Service"
                tommorrow_amc.append({"date": datetime.today().date() + timedelta(days=1), "client": client,
                                      'service_status': service_status, "phone": client_no})
            else:
                service_status = 'Fourth Service'
                tommorrow_amc.append({"date": datetime.today().date() + timedelta(days=1), "client": client,
                                      'service_status': service_status, "phone": client_no})

    if len(tommorrow_amc) == 0:
        return "Tommorrow No AMC Service"
    return tommorrow_amc


def amcAlertMonth(request):
    this_month_amc = []
    data = list(amc.AMC.objects.filter(company_id=request.session.get('company_id')).values(
        'pk').annotate(
        amc_client=F('client_name__name'),
        amc_first_service_date=ExpressionWrapper(Func(F('first_service_date'), Value("MM-YY"), function='TO_CHAR'),
                                                 output_field=CharField()),
        amc_second_service_date=ExpressionWrapper(Func(F('second_service_date'), Value("MM-YY"), function='TO_CHAR'),
                                                  output_field=CharField()),
        amc_third_service_date=ExpressionWrapper(Func(F('third_service_date'), Value("MM-YY"), function='TO_CHAR'),
                                                 output_field=CharField()),
        amc_fourth_service_date=ExpressionWrapper(Func(F('fourth_service_date'), Value("MM-YY"), function='TO_CHAR'),
                                                  output_field=CharField()),
        amc_client_phone=F('client_name__phone'),
    ))

    for each in data:
        if each.get('amc_first_service_date') == datetime.today().date().strftime("%m-%y") \
                or each.get('amc_second_service_date') == datetime.today().date().strftime("%m-%y") \
                or each.get('amc_third_service_date') == datetime.today().date().strftime("%m-%y") \
                or each.get('amc_fourth_service_date') == datetime.today().date().strftime("%m-%y"):
            client_no = each.get('amc_client_phone')
            client = each.get('amc_client')
            this_month_amc.append({"date": datetime.today().date().strftime("%m/%y"), "client": client,
                                   "phone": client_no})

    if len(this_month_amc) == 0:
        return "This Month No AMC Service"
    return this_month_amc
