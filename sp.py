print('Info: ИГРА ОБЛАДАЕТ НАДЁЖНОЙ СТЕПЕНЬЮ ЗАЩИТЫ ОТ ЖУЛЬНИЧЕСТВА')
print('добро пожаловать в игру')
print('1 игра 50 спичек')
print('2 игра 100 спичек')
print('3 кол-во спичек можно выберать ')
print('4 игра 1000 спичек ')
print('5 режим хардкор')

import time
import random

pop = int(input('введите номер игры:    '))
if pop == 1:
    print ("игра 50 спичек")
    всего_спичек = 50
    print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ 50 СПИЧЕК ')

    н = input('как вас зовут      ')
    z = input('как вы будете называть бота       ')
    вопрос = input('кто будет ходить первым        ')
    if вопрос == 'я':
        очередь_хода = True
    else:
        очередь_хода = False
    while всего_спичек > 0:
        if очередь_хода == True:
            взял_спичек = int(input('введите число от 1 до 5        '))
            while взял_спичек > 5 or взял_спичек < 1:
                print('вы ввели неправельное число введите число от 1 до 5')
                взял_спичек = int(input('введите число от 1 до 5            '))
            всего_спичек -= взял_спичек
            очередь_хода = False
        else:
            if всего_спичек > 5:
                взял_спичек = random.randint(1, 5)
                всего_спичек -= взял_спичек
            else:
                взял_спичек = всего_спичек
                всего_спичек -= взял_спичек
            очередь_хода = True
        print(f'В этот ход взяли {взял_спичек} спичек. Осталось {всего_спичек}')
    if очередь_хода == True:
        print("Победил", z)
        input('для выхода нажмите Enter')
    else:
        print(н, "Вы победили")
        input('для выхода нажмите Enter')
        exit()
else:
    if pop == 2:
        print("игра 100 спичек")
        всего_спичек = 100
        print('         ДОБРО ПОЖАЛОВАТЬ В ИГРУ 100 СПИЧЕК')
        print('ЭТО НОВОЕ ОБНОВЛЕНИЕ ВМЕСТО 50 СПИЧЕК ЦЕЛЫХ 100')
        print('ТАК ИГРА СТАЛА ДЛИННЕЕ И ИНТЕРЕСНЕЕ')
        print('скоро выйдет нове обновление где вы можите выбирать кол-во спичек')
        н = input('как вас зовут        ')
        z = input('как вы будете называть бота         ')
        вопрос = input('кто будет ходить первым         ')
        if вопрос == 'я':
            очередь_хода = True
        else:
            очередь_хода = False
        while всего_спичек > 0:
            if очередь_хода == True:
                взял_спичек = int(input('введите число от 1 до 5         '))
                while взял_спичек > 5 or взял_спичек < 1:
                    print('вы ввели неправельное число введите число от 1 до 5')
                    взял_спичек = int(input('введите число от 1 до 5         '))
                всего_спичек -= взял_спичек
                очередь_хода = False
            else:
                if всего_спичек > 5:
                    взял_спичек = random.randint(1, 5)
                    всего_спичек -= взял_спичек
                else:
                    взял_спичек = всего_спичек
                    всего_спичек -= взял_спичек
                очередь_хода = True
            print(f'В этот ход взяли {взял_спичек} спичек. Осталось {всего_спичек}')
        if очередь_хода == True:
            print("Победил", z)
            input('для выхода нажмите Enter')
        else:
            print(н, "Вы победили")
            input('для выхода нажмите Enter')
        exit()
    else:
        if pop == 3:
            print("кол-во спичек можно выберать")
            print('         ДОБРО ПОЖАЛОВАТЬ В ИГРУ ')

            war = int(input('введите кол-во спичек которое будет в игре         '))
            while war < 11:
                print('вы ввели неправельное число введите числокоторое будет не мменьше 10')
                war = int(input('введите кол-во спичек которое будет в игре         '))
            else:

                всего_спичек = war
                н = input('как вас зовут        ')
                z = input('как вы будете называть бота         ')
                вопрос = input('кто будет ходить первым         ')
            if вопрос == 'я':
                очередь_хода = True
            else:
                очередь_хода = False
            while всего_спичек > 0:
                if очередь_хода == True:
                    взял_спичек = int(input('введите число от 1 до 10         '))
                    while взял_спичек > 10 or взял_спичек < 1:
                        print('вы ввели неправельное число введите число от 1 до 10')
                        взял_спичек = int(input('введите число от 1 до 10         '))
                    всего_спичек -= взял_спичек
                    очередь_хода = False
                else:
                    if всего_спичек > 10:
                        взял_спичек = random.randint(1, 10)
                        всего_спичек -= взял_спичек
                    else:
                        взял_спичек = всего_спичек
                        всего_спичек -= взял_спичек
                    очередь_хода = True
                print(f'В этот ход взяли {взял_спичек} спичек. Осталось {всего_спичек}')
            if очередь_хода == True:
                print("Победил", z)
                input('для выхода нажмите Enter')
            else:
                print(н, "Вы победили")
                input('для выхода нажмите Enter')
            exit()
        else:
            if pop == 4:
                print("игра 1000")
                всего_спичек = 1000
                print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ 1000 СПИЧЕК ')

                н = input('как вас зовут      ')
                z = input('как вы будете называть бота       ')
                вопрос = input('кто будет ходить первым        ')
                if вопрос == 'я':
                    очередь_хода = True
                else:
                    очередь_хода = False
                while всего_спичек > 0:
                    if очередь_хода == True:
                        взял_спичек = int(input('введите число от 1 до 50        '))
                        while взял_спичек > 50 or взял_спичек < 1:
                            print('вы ввели неправельное число введите число от 1 до 50')
                            взял_спичек = int(input('введите число от 1 до 50            '))
                        всего_спичек -= взял_спичек
                        очередь_хода = False
                    else:
                        if всего_спичек > 50:
                            взял_спичек = random.randint(1, 50)
                            всего_спичек -= взял_спичек
                        else:
                            взял_спичек = всего_спичек
                            всего_спичек -= взял_спичек
                        очередь_хода = True
                    print(f'В этот ход взяли {взял_спичек} спичек. Осталось {всего_спичек}')
                if очередь_хода == True:
                    print("Победил", z)
                    input('для выхода нажмите Enter')
                else:
                    print(н, "Вы победили")
                    input('для выхода нажмите Enter')
            else:
                if pop == 5:
                    print('игра хардкор')
                    print('         ДОБРО ПОЖАЛОВАТЬ В ИГРУ ХАРДКОР ')
                    print('ЭТО НОВОЕ ОБНОВЛЕНИЕ.В ИГРЕ ПОЯВИЛСЯ РЕЖИМ ХАРДКОР ТАК ИГРА СТАЛА СУМАШЕДШЕЙ ')
                    print('скоро выйдет нове обновление но это не точно')

                    всего_спичек = 1000000000000
                    н = input('как вас зовут        ')
                    z = input('как вы будете называть бота         ')
                    вопрос = input('кто будет ходить первым         ')
                    if вопрос == 'я':
                        очередь_хода = True
                    else:
                        очередь_хода = False
                    while всего_спичек > 0:
                        if очередь_хода == True:
                            взял_спичек = int(input('введите число от 1 до 100000         '))
                            while взял_спичек > 100000 or взял_спичек < 1:
                                print('вы ввели неправельное число введите число от 1 до 100000')
                                взял_спичек = int(input('введите число от 1 до 100000         '))
                            всего_спичек -= взял_спичек
                            очередь_хода = False
                        else:
                            if всего_спичек > 10000:
                                взял_спичек = random.randint(1, 100000)
                                всего_спичек -= взял_спичек
                            else:
                                взял_спичек = всего_спичек
                                всего_спичек -= взял_спичек
                            очередь_хода = True
                        print(f'В этот ход взяли {взял_спичек} спичек. Осталось {всего_спичек}')
                    if очередь_хода == True:
                        print("Победил", z)
                        input('для выхода нажмите Enter')
                    else:
                        print(н, "Вы победили")
                        input('для выхода нажмите Enter')
                    exit()

