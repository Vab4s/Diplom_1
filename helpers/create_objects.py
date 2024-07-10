import random
import allure
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database


@allure.step('Создание объекта Bun')
def create_bun():
    name = 'test_bun'
    price = random.uniform(0, 99)
    new_bun = Bun(name, price)
    return new_bun, name, price

@allure.step('Создание объекта Burger')
def create_burger():
    new_burger = Burger()
    return new_burger

@allure.step('Создание объекта Database')
def create_database():
    new_database = Database()
    return new_database
