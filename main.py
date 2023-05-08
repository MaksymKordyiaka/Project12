'''
Створити клас, задавши три атрибути з різними модифікаторами доступу, при чому «публічний» атрибут
встановлено за замовчуванням.

Створити методи, для редагування кожного з атрибутів. При роботі даних методів- в окремий текстовий
файл буде «!!!дозаписуватись!!!» інформація про те, який об’єкт та коли вносить редагування для атрибутів.

Для цього можна використати:

from datetime import datetime
datetime.now()

Час зміни вказуємо до секунди (мілісекунди відкидаємо)
'''

from datetime import datetime
text = open('text.txt', 'w')
class Main:
    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value
        text.write(f'object _y: {datetime.now().replace(microsecond=0)}\n')

    def get_z(self):
        return self.__z

    def set_z(self, value):
        self.__z = value
        text.write(f'object __z: {datetime.now().replace(microsecond=0)}')

a = Main(3, 30, 300)
print(a.x)
print(a.get_y())
print(a.get_z())
a.x = 4
text.write(f'object x: {datetime.now().replace(microsecond=0)}\n')
a.set_y(50)
a.set_z(600)
print(a.x)
print(a.get_y())
print(a.get_z())
