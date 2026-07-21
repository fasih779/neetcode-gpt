import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        v = []
       

        for i in range(len(z)):
            value = 1 / (1 + np.exp(-z[i]))
            v.append(value)
        return np.round(v, 5)
        

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        r=[]
        for i in range(len(z)):
            p=max(0.0,z[i])
            r.append(p)
        return np.round(r,5)
        
