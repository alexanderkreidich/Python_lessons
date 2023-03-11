def check_tax(user_money, property_tax):
    if user_money > property_tax:
        print('Сумма налога за машину равен: {}\nУ вас хватает денег на оплату налога.'.format(property_tax))
    else:
        print('Сумма налога за машину равен: {}\nУ вас не хватает денег на оплату налога.'.format(property_tax))


class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth

    def get_tax(self, user_money):
        tax = self.worth / 1000
        check_tax(user_money, tax)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth

    def get_tax(self, user_money):
        tax = self.worth / 200
        check_tax(user_money, tax)
class CountryHouse(Property):
    def __init__(self, worth):
        super(CountryHouse, self).__init__(worth)
        self.worth = worth

    def get_tax(self, user_money):
        tax = self.worth / 500
        check_tax(user_money, tax)


def main():
    money = int(input('Какое количество денег у вас на счету? '))
    user_car = Car(worth=int(input('Сколько стоит ваша машина? ')))
    user_house = CountryHouse(worth=int(input('Сколько стоит ваш загородный дом? ')))
    user_apart = Apartment(worth=int(input('Сколько стоит ваша квартира? ')))
    while True:
        ask = input('\nПро какую сумму налога вы хотите узнать?\n1.Машина\n2.Квартира\n3.Загородный дом\n').lower()
        if ask == 'машина':
            user_car.get_tax(money)
        elif ask == 'квартира':
            user_apart.get_tax(money)
        elif ask == 'загородный дом':
            user_house.get_tax(money)
        ask = input('Хотите продолжать? да/нет: ').lower()
        if ask == 'да':
            continue
        else:
            break

main()
