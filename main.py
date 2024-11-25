from cardloto import Cardloto
import numpy as np


print('Запускаем игру лото')

def random_element(array):
    # Выбираем случайный элемент
    random_element = np.random.choice(array)

    # Удаляем выбранный элемент из массива
    array = np.delete(array, np.where(array == random_element)[0][0])

    return random_element

def answer():
    while 1:
        try:
            ans = int(input('Есть ли боченок на карточке (0 - нет, 1 - да): '))
            if ans not in [0, 1]:
                raise ValueError  # Генерируем исключение, если введено не 0 и не 1
            return ans
        except ValueError:
            print('Вы ввели не 0 или 1, попробуйте снова')

# Создаем озновные переменные
gamer_card = Cardloto('Gamer')
computer_card = Cardloto('Computer')
numbers = np.arange(1, 91)
game_finish = True

# Запускаем игру
while game_finish:

    number = random_element(numbers)
    computer_card.check_keg(number)
    computer_card.show_card()
    gamer_card.show_card()

    print('Выпал боченок - ', number)
    ans = answer()
    check = gamer_card.check_keg(number)
    if (ans and check) or (not ans and not check):
        computer_card.check_keg(number)
    elif not check:
        print('Нет такого боченка, Вы проиграли')
        break
    else:
        print('Вы пропустили боченок, Вы проиграли')
        break

    print()

    if computer_card.get_close() or gamer_card.get_close():
        game_finish = False




