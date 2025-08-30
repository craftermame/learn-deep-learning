import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7  # np.log(0)となることを防止
    return -np.sum(t*np.log(y+delta))


def test():
    # 0-5の手描き文字の分類問題を想定
    t = np.array([0, 0, 1, 0, 0])  # 2 が正解とする

    y = np.array([0.1, 0.2, 0.5, 0.1, 0.1])  # softmax関数の出力の例（2の確率が一番高い）
    print('Mean Squared Error:', mean_squared_error(y, t))  # 0.16  # 誤差がより小さい
    print('Cross Entropy Error:', cross_entropy_error(y, t))  # 0.6931469805599654

    print('='*80)

    y = np.array([0.1, 0.2, 0.1, 0.1, 0.5])  # softmax関数の出力の例（5の確率が一番高い）
    print('Mean Squared Error:', mean_squared_error(y, t))  # 0.56  # 誤差がより大きい
    print('Cross Entropy Error:', cross_entropy_error(y, t))  # 2.302584092994546

if __name__ == '__main__':
    test()
