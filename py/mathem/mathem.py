import math

# ceil(x) 	Возвращает округленное x как ближайшее целое значение типа int, большее или равное x (округление "вверх").
# fabs(x) 	Возвращает абсолютное значение (модуль) числа x. В Python есть встроенная функция abs, но она возвращает модуль числа с тем же типом, что число, здесь же всегда float abs (fabs).
# factorial(x) 	Возвращает факториал целого числа x, если x не целое возбуждается исключение ValueError.
# floor(x) 	В противоположность ceil(x) возвращает округленное x как ближайшее целое значение типа int, меньшее или равное x (округление "вниз").
# frexp(x) 	Представляет число в экспоненциальной записи
# и возвращает мантиссу m (действительное число, модуль которого лежит в интервале от 0.5 включительно до 1 не включительно) и порядок n (целое число) как пару чисел (m, n). Если x=0, то возвращает (0.0, 0)
# fsum(iterable) 	Возвращает float сумму от числовых элементов итерируемого объекта.
# isinf(x) 	Проверяет, является ли float объект x плюс или минус бесконечностью, результат соответственно True или False.
# isnan(x) 	Проверяет, является ли float объект x объектом NaN (not a number).
# ldexp(x, i) 	Возвращает значение, то есть осуществляет действие, обратное функции frexp(x).
# modf(x) 	Возвращает дробную и целую часть float числа. Оба результата сохраняют знак исходного числа x и представлены типом float.
# trunc(x) 	Возвращает целую часть числа x в виде int объекта.


# Степенные и логарифмические функции
# exp(x) 	Возвращает.
# log(x[, base]) 	При передаче функции одного аргумента x, возвращает натуральный логарифм x (логарифм по основанию e = 2.7182…). При передаче двух аргументов, второй берется как основание логарифма.
# log10(x) 	Возвращает десятичный логарифм x.
# pow(x, y) 	Возвращает x в степени y. В отличие от операции ** приводит оба аргумента к типу float.
# sqrt(x) 	Квадратный корень (square root) из x.

# Тригонометрические функции
# acos(x) 	Возвращает арккосинус x, в радианах.
# asin(x) 	Возвращает арксинус x, в радианах.
# atan(x) 	Возвращает арктангенс x, в радианах.
# atan2(y, x) 	Возвращает, в радианах. Результат лежит в интервале [-&pi;, &pi;]. Вектор, конец, которого задается точкой (x, y) образует угол с положительным направлением оси x. Поэтому эта функция имеет более общее назначение, чем предыдущая. Например и atan(1), и atan2(1, 1) дадут в результате pi/4, но atan2(-1, -1) это уже -3*pi/4.
# cos(x) 	Возвращает косинус x, где x выражен в радианах.
# hyp(x, y) 	Возвращает sqrt(x**2+y**2). Удобно для вычисления гипотенузы (hyp) и длины вектора.
# sin(x) 	Возвращает синус x, где x выражен в радианах.
# tan(x) 	Возвращает тангенс x, где x выражен в радианах.


# Радианы в градусы и наоборот
# degrees(x) 	Конвертирует значение угла x из радиан в градусы.
# radians(x) 	Конвертирует значение угла x из градусов в радианы.

# Пример программы с математическими функциями

from math import *   # Импортируем библиотеку math


def my_function(x):
    x = fabs(x) # Наша функция будет четной
    y = sqrt(x) # Извлекаем корень квадратный
    y = exp(sin(y) + 1) # Берем синус, прибавляем 1, а затем это выражение сразу в показатель экспоненты
    return y

print(my_function(2))

# А можно написать эту функцию так (в функциональном стиле):

from math import *


def my_function(x):
    return exp(sin(sqrt(fabs(x))) + 1)

print(my_function(2))

