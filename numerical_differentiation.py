
def numerical_diff(f, x):
    h = 1e-4  # 0.0001（差分は小さすぎなくていい）
    return (f(x+h) - f(x-h)) / (2*h)


def test():
    import numpy as np
    import matplotlib.pyplot as plt

    def function_1(x):
        return 0.01*x**2 + 0.1*x

    x = np.arange(0.0, 20.0, 0.1)

    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    y1 = function_1(x)
    axes[0].plot(x, y1)
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('f(x)')
    axes[0].set_title('Primitive Function')  # 原始関数

    y2 = numerical_diff(function_1, x)
    axes[1].plot(x, y2)
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('f\'(x)')
    axes[1].set_title('Derivative Function')  # 導関数

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test()
