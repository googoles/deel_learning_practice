import numpy as np


# 가중치 편향을 사용한 AND게이트

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와 w,b의 부호만 바꾼것
    b = 0.7

    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND와 w,b의 부호만 바꾼것
    b = -0.2

    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# Result = 3가지 게이트는 모두 같은 구조의 Perceptron이다!

#2.5.1 XOR Gate
# NAND와 OR 그리고 AND게이트를 합쳐서 구성한 XOR게이트

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))

# XOR은 다층 퍼셉트론이다!
