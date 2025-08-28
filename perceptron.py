import numpy as np

def perceptron(x1, x2, w1, w2, b):
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    return 1

def OR(x1, x2):
    return perceptron(x1, x2, 0.2, 0.2, -0.1)

def AND(x1, x2):
    return perceptron(x1, x2, 0.1, 0.1, -0.1)

def NAND(x1, x2):
    return perceptron(x1, x2, -0.1, -0.1, 0.2)

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


def test():

    assert OR(0, 0) == 0
    assert OR(0, 1) == 1
    assert OR(1, 0) == 1
    assert OR(1, 1) == 1
    print('OR is correct!')

    assert AND(0, 0) == 0
    assert AND(0, 1) == 0
    assert AND(1, 0) == 0
    assert AND(1, 1) == 1
    print('AND is correct!')

    assert NAND(0, 0) == 1
    assert NAND(0, 1) == 1
    assert NAND(1, 0) == 1
    assert NAND(1, 1) == 0
    print('NAND is correct!')

    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0
    print('XOR is correct!')


if __name__ == '__main__':
    test()
