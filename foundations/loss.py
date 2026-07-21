import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        epsilon=1e-7
        y_pred=np.clip(y_pred,epsilon,1-epsilon)
        loss=np.sum(y_true*np.log(y_pred)+(1-y_true)*np.log(1-y_pred))
        return np.round(-(loss/len(y_true)),4)
        
        pass

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        epsilon = 1e-7
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

        loss = -np.sum(y_true * np.log(y_pred)) / len(y_true)

        return round(loss, 4)
        pass
