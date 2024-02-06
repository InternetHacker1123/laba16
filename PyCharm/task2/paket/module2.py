#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(sp):
    punkt_naznachenia = input("Пункт назначения поезда: ")
    train_number = input("Номер поезда: ")
    time_otpravlenia = input("Время отправления: ")

    dictionary = {
        'Пункт назначения ': punkt_naznachenia,
        'Номер поезда: ': train_number,
        'Время отправления:': time_otpravlenia
    }

    sp.append(dictionary)
    sp = sorted(sp, key=lambda x: x['Номер поезда: '])

def choose(sp):
    inp = input("Введите номер поезда: ")
    for d in sp:
        if inp in d.values():
            print(d)
        else: 
            print('Поезда с таким номером нет')

def get_list(sp):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
    '-' * 4,
    '-' * 30,
    '-' * 20,
    '-' * 20
    )
    print(line)
    print(
    '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
        "№",
        "Пункт назначения",
        "Номер поезда",
        "Время отправления"
        )
    )
    print(line)
    for idx, train in enumerate(sp, 1):
        print(
        '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
            idx,
            train.get('Пункт назначения ', ''),
            train.get('Номер поезда: ', ''),
            train.get('Время отправления:', 0)
            )
        )
        print(line)

def help():
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("choose - найти поезд с заданным номером")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    sp = []
    while True:
        inp = input(">>> ").lower()
        match inp:
            case 'add':
                add(sp)
            case 'list':
                get_list(sp)
            case 'help':
                help()
            case 'choose':
                choose(sp)
