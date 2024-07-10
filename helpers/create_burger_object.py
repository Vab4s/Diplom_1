import allure
from praktikum.burger import Burger


@allure.step('Создание объекта Burger')
def create_burger():
    new_burger = Burger()
    return new_burger
