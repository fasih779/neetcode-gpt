import numpy as np
from typing import List


class Solution:
    def forward_and_backward(self,
                              x: List[float],
                              W1: List[List[float]], b1: List[float],
                              W2: List[List[float]], b2: List[float],
                              y_true: List[float]) -> dict:
        z1 = np.dot(x, np.transpose(W1)) + b1
        a1 = np.maximum(0, z1)

        z2 = np.dot(a1, np.transpose(W2)) + b2
        loss = np.mean((z2 - y_true) ** 2)


        n = len(y_true)

        dz2 = 2 * (z2 - y_true) / n

        db2 = dz2

        dW2 = np.outer(dz2, a1)

        da1 = np.dot(dz2, W2)

        dz1 = da1 * (z1 > 0)

        db1 = dz1

        dW1 = np.outer(dz1, x)
        return {
                "loss": round(loss, 4),
                "dW1": np.round(dW1, 4).tolist(),
                "db1": np.round(db1, 4).tolist(),
                "dW2": np.round(dW2, 4).tolist(),
                "db2": np.round(db2, 4).tolist(),
                    }