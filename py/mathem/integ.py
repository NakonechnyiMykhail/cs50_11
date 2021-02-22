import random as random_number
import matplotlib.pyplot as plt
from numpy import array, linspace
import random 

def MCint3(f, a, b, n, N=100):
    '''Cохраняет каждое N приближение интеграла
    в массив I и записываем соответствующее значение k'''
    s = 0

    I_values = []
    k_values = []
    for k in range(1, n+1):
        x = random_number.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k)*s
            I_values.append(I)
            k_values.append(k)
    return k_values, I_values

def MCint_vec(f, a, b, n):
    x = random.uniform(a, b, n)
    s = sum(f(x))
    I = (float(b-a)/n)*s
    return I

def f1(x):
    return 2 + x*x

a = -30
b = 30
n = 1000000

k, I = MCint3(f1, a, b, n, N=10000)
# error = 6.5 - array(I)

t = linspace(a, b, n) 
y = f1(t)

plt.title('Monte Carlo integration')
plt.xlabel('n')
plt.ylabel('error')
plt.plot(y, I)
plt.show()




# plt.plot(t, y)
# plt.show()