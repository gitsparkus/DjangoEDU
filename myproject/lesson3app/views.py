from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from lesson3app.models import Client, Good, Order
from datetime import date, timedelta, datetime


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)

    context = {"client": client,
               "orders": orders}

    return render(request, "lesson3app/client_orders.html", context)


def client_goods(request, client_id, days):
    date_end = datetime.now()
    date_start = date_end - timedelta(days=days)

    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client, date_ordered__range=(date_start, date_end)).order_by('date_ordered')
    goods_list = []

    for order in orders:
        goods = order.goods.all()
        for good in goods:
            if good not in goods_list:
                goods_list.append(good)

    context = {"client": client,
               "goods": goods_list,
               "days": days}

    return render(request, "lesson3app/client_goods.html", context)
