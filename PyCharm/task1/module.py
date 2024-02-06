#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def outer_function(f):
    def inner_function(a, b):
        result = f(a, b)
        return f"Для значений {a}, {b} функция f({a}, {b}) = {result}"
    return inner_function


# Пример функции f, которую мы передадим во внешнюю функцию
def my_function(a, b):
    return a * b + a - b


# Главная функция
def main():
    closure = outer_function(my_function)
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(closure(a, b))