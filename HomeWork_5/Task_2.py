# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
#
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
import random

def player_vs_player():

    name_1 = input("Введите имя первого игрока: ")
    name_2 = input("Введите имя второго игрока: ")
    candies = int(input("Введите количество конфет: "))
    max_move = 28
    count_check_win = candies // max_move

    priority = random.randrange(1, 3)
    if priority == 1:
        print(f"{name_1} ходит первым")
    else:
        print(f"{name_2} ходит первым")

    win = False
    while not win:
        if priority % 2 == 0:
            candies = players_move(name_2, candies, max_move)
        else:
            candies = players_move(name_1, candies, max_move)

        if priority >= count_check_win - 1:
            temp = check_win(candies, priority, name_1, name_2)
            if temp:
                print(f'{temp} выиграл')
                win = True
        priority += 1

def players_move (name_player, candies, max_move):
    valid = False
    while not valid:
        players_move = int(input(f"{name_player}, сколько конфет ты возьмешь(1-28): "))
        if players_move > 0 and players_move <= max_move and players_move <= candies:
            print(f'{name_player} забрал {players_move} конфет')
            candies -= players_move
            print(f'Осталось {candies} конфет')
            valid = True
        else:
            print(f'Количество взятых конфет должно быть в интервале от 1 до {max_move} или не больше оставшегося количества конфет')
        return candies

def check_win(candies, priority, name_1, name_2):
    if candies == 0:
        return name_1 if priority % 2 == 0 else name_2
    else:
        return False

player_vs_player()