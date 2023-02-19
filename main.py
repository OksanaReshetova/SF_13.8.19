sum1 = 990
sum2 = 1390
ticket = int (input('Введите количество билетов: '))
age = int(input('Введите возраст: '))
while ticket <= 3:
    if age >= 18 and age <= 25:
        price = ticket * sum1
        print('Цена билета:', int(price), 'руб.')
    elif age > 25:
        price = ticket * sum2
        print('Цена билета:', int(price), 'руб.')
    break

if ticket > 3 and (age >= 18 and age <= 25):
    price = ticket * (sum1 - (sum1 /100 * 10))
    print('Цена билета:', int(price), 'руб.')
elif ticket > 3 and age > 25:
    price = ticket * (sum2 - (sum2 / 100 * 10))
    print('Цена билета:', int(price), 'руб.')
elif age < 18:
        print('Бесплатный билет')