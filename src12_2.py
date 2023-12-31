"""
Использование методов-сопрограмм очереди
с. 333
"""
import asyncio
from asyncio import Queue
from random import randrange


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_numer: int):
    while not queue.empty():
        customer: Customer = queue.get_nowait()
        print(f'Кассир {cashier_numer} начал обслуживать покупателя {customer.customer_id}')
        for product in customer.products:
            print(f'Кассир {cashier_numer} обслуживает покупателя {customer.customer_id}: {product.name}')
            await asyncio.sleep(product.checkout_time)
        print(f'Кассир {cashier_numer} закончил обслуживать покупателя {customer.customer_id}')
        queue.task_done()


def generate_customer(customer_id: int) -> Customer:
    all_products = [
        Product('Пиво', 2),
        Product('Бананы', .5),
        Product('Колбаса', .2),
        Product('Подгузники', .2),
    ]
    products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    return Customer(customer_id, products)


async def customer_generator(queue: Queue):
    customer_count = 0

    while True:
        customers = [generate_customer(i) for i in range(customer_count, customer_count + randrange(5))]
        for customer in customers:
            print('Ожидаю возможности поставить покупателя в очередь...')
            await queue.put(customer)
            print('Покупатель поставлен в очередь!')
        customer_count += len(customers)
        await asyncio.sleep(1)


async def main():
    customer_queue = Queue()

    customer_producer = asyncio.create_task(customer_generator(customer_queue))

    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]

    await asyncio.gather(customer_producer, *cashiers)


asyncio.run(main())
