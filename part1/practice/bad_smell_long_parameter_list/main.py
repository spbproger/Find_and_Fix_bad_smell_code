# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, x_coord, y_coord, speed: int, state: str):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.state = state
        self.speed = self._get_speed(self.state, speed)

    def move(self, direction: str):
        if direction.upper() == 'UP':
            self.y_coord += self.speed
        elif direction.upper() == 'DOWN':
            self.y_coord -= self.speed
        elif direction.upper() == 'LEFT':
            self.x_coord -= self.speed
        elif direction.upper() == 'RIGTH':
            self.x_coord += self.speed

        return self.x_coord, self.y_coord

    def _get_speed(self, state, speed):
        if state == 'fly':
            return speed * 1.2
        elif state == 'crawl':
            return speed * 0.5
        else:
            raise ValueError('Нет такого способа передвижения')
