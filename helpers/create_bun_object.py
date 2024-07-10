import random
import allure
from praktikum.bun import Bun


@allure.step('Создание объекта Bun')
def create_bun():
    name = 'test_bun'
    price = random.uniform(0, 99)
    new_bun = Bun(name, price)
    return new_bun, name, price
