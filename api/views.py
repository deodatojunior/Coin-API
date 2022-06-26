from django.shortcuts import render, redirect
import requests as req
link = 'https://economia.awesomeapi.com.br/json/'
link_alt = 'https://economia.awesomeapi.com.br/'


def initial_form(request):
    if request.method == 'POST':
        code = request.POST['code']
        quantity = request.POST['quantity']
        days = request.POST['days']
        if code != "" and quantity != "":
            return redirect('get_info_coin_by_code_and_quantity', coin=code, quantity=quantity)
        elif code != "" and days != "":
            return redirect('get_info_coin_by_code_and_days', coin=code, days=days)
        elif code != "":
            return redirect('get_info_coin_by_code_in_realtime', coin=code)
    return render(request, 'base.html')


def get_info_coin_by_code_and_quantity(request, coin, quantity):
    connect = req.get(link + f"{coin}/{quantity}")
    response = connect.json()
    return render(request, 'get_info_coin_by_code_and_quantity.html', {'list': response})


def get_info_coin_by_code_and_days(request, coin, days):
    connect = req.get(link_alt + f"json/daily/{coin}/{days}")
    response = connect.json()
    return render(request, 'get_info_coin_by_code_and_days.html', {'list': response})


def get_info_coin_by_code_in_realtime(request, coin):
    connect = req.get(link_alt + f"last/{coin}/")
    response = connect.json()
    return render(request, 'get_info_coin_by_code_in_realtime.html', {'list': response.items()})
