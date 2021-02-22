# # Program for computing the height of a ball thrown up in the air.  
# v0 = 5     # Initial velocity
# g = 9.81   # Acceleration of gravity
# t = 0.6    # Time
# y = v0*t - 0.5*g*t**2  # Vertical position
# print  (y)

# импортируем модуль для работы с математическими функциями
# для быстрых вычислений следует использовать модуль cmath
# в отличии от math - cmath является не скриптом, а исполняемым файлом
import math

v0 = 5
g = 9.81
yc = 0.2

# используем функцию извлечения корня квадратного - math.sqrt
t1 = (v0 - math.sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + math.sqrt(v0**2 - 2*g*yc))/g
print('At t=%g s and %g s, the height is %g m.' % (t1, t2, yc))