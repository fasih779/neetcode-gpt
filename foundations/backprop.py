from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(
        self,
        x: NDArray[np.float64],
        w: NDArray[np.float64],
        b: float,
        y_true: float
    ) -> Tuple[NDArray[np.float64], float]:

       
        z = np.dot(x, w) + b
        y_hat = 1 / (1 + np.exp(-z))

      
        delta = (y_hat - y_true) * y_hat * (1 - y_hat)

        
        dw = delta * x

        
        db = delta

        return np.round(dw, 5), round(db, 5)