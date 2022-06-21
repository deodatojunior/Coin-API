from django.http import HttpResponse
import requests as req
link = 'https://economia.awesomeapi.com.br/json/'
link_alt = 'https://economia.awesomeapi.com.br/'


def get_info_coin_by_code_and_quantity(request, coin, quantity):
    connect = req.get(link + f"{coin}/{quantity}")
    response = connect.json()
    return HttpResponse(response)


def get_info_coin_by_code_and_days(request, coin, days):
    connect = req.get(link_alt + f"json/daily/{coin}/{days}")
    response = connect.json()
    return HttpResponse(response)


def get_info_coin_by_code_in_realtime(request, coin):
    connect = req.get(link_alt + f"last/{coin}/")
    response = connect.json()
    return HttpResponse(response.items())
