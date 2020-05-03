import csv
import sys
from typing import Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def step_gradient_descent(
    training_data: Sequence[Tuple[float, float]],
    w: float,
    b: float,
    alpha: float
) -> Tuple[float, float]:
    n = len(training_data)

    # partial derivative of MSE wrt w
    pdw = sum([-2 * x * (y - (w * x + b)) for (x, y) in training_data]) / n
    new_w = w - alpha * pdw

    # partial derivative of MSE wrt b
    pdb = sum([-2 * (y - (w * x + b)) for (x, y) in training_data]) / n
    new_b = b - alpha * pdb

    return (new_w, new_b)


def mse(
    training_data: Sequence[Tuple[float, float]],
    w: float,
    b: float
) -> float:
    n = len(training_data)

    return sum([pow(y - (w * x + b), 2) for (x, y) in training_data]) / n


if __name__ == "__main__":
    datafile = sys.argv[1]
    epochs = int(sys.argv[2])

    training_data = []
    with open(datafile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            spending = float(row["radio"])
            sales = float(row["sales"])
            training_data.append((spending, sales))

    w = 0.0
    b = 0.0
    alpha = 0.001

    for epoch in range(epochs):
        (new_w, new_b) = step_gradient_descent(training_data, w, b, alpha)
        w = new_w
        b = new_b
        loss = mse(training_data, w, b)

        if epoch % 100 == 0:
            print(f"epoch={epoch}, loss={loss}")

    # Viz
    sns.set(style="darkgrid")
    df = pd.DataFrame(training_data, columns=["spending", "sales"])
    plot = sns.relplot(x="spending", y="sales", data=df)

    # All this just to visualize a line..
    x = np.linspace(0, plt.xlim()[1], 1000)
    plt.plot(x, w * x + b)
    plt.show()
