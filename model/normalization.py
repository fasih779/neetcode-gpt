import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], gamma: NDArray[np.float64], beta: NDArray[np.float64]) -> NDArray[np.float64]:
        eps = 1e-5

        # Calculate mean
        mean = np.mean(x)

        # Calculate variance
        var = np.mean((x - mean) ** 2)

        # Normalize
        x_hat = (x - mean) / np.sqrt(var + eps)

        # Scale and shift
        out = gamma * x_hat + beta

        return np.round(out, 5)
