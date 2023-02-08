# 2. Написать функцию для перевода доллара в евро c округлением до 2х знаков
# после запятой, если известно, что текущий курс составляет 1.17 долларов за
# один евро.


def dollarsToEuro(idx=1.17):
    flag = True
    while flag:
        try:
            dollars = input('Введите количество долларов >>> ')
            if dollars == 'q':
                print('До свидания!')
                flag = False
            euro = round(float(dollars) / idx, 2)
            print(f"Вы получите: {euro} евро.")
            flag = False

        except ValueError:
            print(f"Неправильный формат. Попробуйте ещё раз.\nДля выхода нажмите 'q'")

dollarsToEuro()
