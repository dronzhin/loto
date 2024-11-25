import numpy as np
import random

class Cardloto:

    def __init__(self, name = 'My card'):
        self.__card = np.zeros((3, 9), dtype=int)  # Создаем пустую карточку
        self.__generate()                                # Генерируем 15 цифр
        self.__del_keg = []                              # Создаем список, куда каписываем боченки, которые вычеркнули с карты
        self.name = name                                 # Название карточки
        self.__close_card = False                        # Закрыта ли вся карта

    def __generate(self):
        for pole in range(3):
            count = 5  # Каждое поле вмещает 5 цифр
            for zona in range(3):
                if count == 0:
                    break

                count_zone = self.__get_count_zone(count, zona)
                count -= count_zone

                numbers = self.__generate_numbers(pole, zona, count_zone)
                sorted_numbers = np.sort(numbers)

                # Генерируем строки, где будут находиться числа
                str_number = np.random.choice(np.arange(0, 3), size=count_zone, replace=False)

                # Вставляем цифры в карточку
                self.__insert_numbers(sorted_numbers, str_number, zona, pole)

    def __get_count_zone(self, count, zona):
        # Определяет количество чисел для текущей зоны.
        count_zone = random.randint(1, min(3, count))
        if zona == 2:
            count_zone = count
        if zona != 2 and count == count_zone:
            count_zone -= 1
        return count_zone

    def __generate_numbers(self, pole, zona, count_zone):
        # Генерирует лучайные числа для указанной зоны.
        if pole == 0 and zona == 0:
            return np.random.choice(np.arange(1, 10), size=count_zone, replace=False)
        else:
            num_zone = zona * 10 + pole * 30
            return np.random.choice(np.arange(num_zone, num_zone + 10), size=count_zone, replace=False)

    def __insert_numbers(self, sorted_numbers, str_number, zona, pole):
        # Вставляет сгенерированные числа в карточку.
        for count_numbers, s in enumerate(str_number):
            self.__card[s, zona + pole * 3] = sorted_numbers[count_numbers]

    def check_keg(self, number):
        if np.any(self.__card == number):
            self.__card[self.__card == number] = -1
            self.__del_keg.append(number)
            self.__close_card = np.all(self.__card < 1)
            return True
        return False

    def show_card(self):
        print(self.name)
        print('-' * 35)
        for i in range(3):
            array_str = np.array2string(self.__card[i], separator=', ', suppress_small=True)
            print(array_str[1:-1].replace(',', ' ').replace('-1', '--').replace(' 0', '  '))
        print('-' * 35)


    def get_card(self):
        return self.__card

    def get_del_keg(self):
        return self.__del_keg

    def get_close(self):
        return self.__close_card

if __name__ == '__main__':
    my_loto = Cardloto()
    my_loto.show_card()
    print(my_loto.check_keg(15))
    my_loto.show_card()
    card = my_loto.get_card()
    print(card[card>0])