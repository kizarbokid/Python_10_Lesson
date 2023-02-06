#!/usr/bin/env python
# coding: utf-8

#     Дана функция f(x) = 5*x**2+10*x-30
# 
#     Определить корни
#     Найти интервалы, на которых функция возрастает
#     Найти интервалы, на которых функция убывает
#     Построить график
#     Вычислить вершину
#     Определить промежутки, на котором f > 0
#     Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

a, b, c = 5, 10, -30


def func(x):
    return a * x ** 2 + b * x + c


limit = 5
step = 0.001

x = np.arange(-limit, limit, step)


def take_roots(a, b, c) -> tuple:
    discr = (b ** 2 - 4 * a * c)
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return round(x1, 4), round(x2, 4)
    elif discr == 0:
        x = -b / (2 * a)
        return (round(x, 4),)
    else:
        return (None,)


roots = take_roots(a, b, c)
print(roots)

min_y = min(func(x))
min_x = take_roots(a, b, c - min_y)[0]

x_down_pos = np.arange(-limit, min(roots), step)
x_down_neg = np.arange(min(roots), min_x, step)

x_up_pos = np.arange(min_x, max(roots), step)
x_up_neg = np.arange(max(roots), limit, step)

plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x_up_pos, func(x_up_pos), 'g', label='возрастание < 0')
plt.plot(x_down_neg, func(x_down_neg), 'r', label='убывание < 0')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_up_neg, func(x_up_neg), 'g', label='возрастание > 0')
plt.plot(x_down_pos, func(x_down_pos), 'r', label='убывание > 0')

if len(roots) == 2:
    plt.plot(roots[0], 0, 'bh', label=f'корни {roots[0]}, {roots[1]}')
    plt.plot(roots[1], 0, 'bh')
else:
    if roots[0] != None:
        plt.plot(roots[0], 0, 'bh', label=f'корень {roots[0]}')

plt.plot(min_x, min_y, 'bx', label=f'Экстремум ({min_x},{min_y})')
plt.legend()
plt.grid()
plt.show()
