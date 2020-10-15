"""
正弦信号
"""
import numpy as np
from sympy import plot, sin, Symbol
t = Symbol('t')  # 定义符号变量t
y = sin(np.pi/4*t)
plot(y)
