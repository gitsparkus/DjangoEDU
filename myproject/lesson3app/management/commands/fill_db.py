import random
from django.core.management.base import BaseCommand
from lesson3app.models import Client, Good, Order


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            good = Good(name=f'name{i}', description=f'description{i}',
                        price=100, quantity=4)
            good.save()

        for i in range(1, count + 1):
            client = Client(name=f'name{i}', email=f'email{i}',
                            phone=f'phone{i}', address=f'address{i}')
            client.save()

            for j in range(1, count + 1):

                order = Order(
                    client=client,
                    total=0,
                )

                order.save()

                for k in range(1, random.randint(1, count)):
                    order.goods.add(Good.objects.get(id=k))
