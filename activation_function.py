import numpy as np

def step(x):
    return np.array(x > 0, dtype=np.int64)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):  # ReLU: Rectified Linear Unit
    return np.maximum(0, x)

def identify_function(x):
    return x


def test():
    from dataclasses import dataclass
    from typing import Any
    import matplotlib.pyplot as plt

    @dataclass
    class MyGraph:
        func: Any
        title: str
        ylim: tuple[float, float]

    graphs = [
        MyGraph(step,    'Step',    (-0.1, 1.1)),
        MyGraph(sigmoid, 'Sigmoid', (-0.1, 1.1)),
        MyGraph(relu,    'ReLU',    (-0.5, 5.5))
    ]

    x = np.arange(-5.0, 5.0, 0.1)
    fig, axes = plt.subplots(len(graphs), 1)
    for i, graph in enumerate(graphs):
        y = graph.func(x)
        axes[i].plot(x, y)
        axes[i].set_title(graph.title)
        axes[i].set_ylim(graph.ylim)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test()
