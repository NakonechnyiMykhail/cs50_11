# from numpy import *
# import matplotlib.pyplot as plt

# def f(t):
#     return t**2*exp(-t**2)

# t = linspace(0, 3, 51)  # 51 точка между 0 и 3
# y = f(t)

# plt.plot(t, y)
# plt.show()

from numpy import *
import matplotlib.pyplot as plt

t = linspace(0, 3, 51)
y1 = t**2*exp(-t**2)
y2 = t**4*exp(-t**2)
y3 = t**6*exp(-t**2)

plt.plot(t, y1, 'g^',    # маркеры из зеленых треугольников
         t, y2, 'b--',   # синяя штриховая
         t, y3, 'ro-')   # красные круглые маркеры, 
                         # соединенные сплошной линией

plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)',
            't^4*exp(-t^2)',
            't^6*exp(-t^2)'],    # список легенды
            loc='upper left')    # положение легенды

plt.show()