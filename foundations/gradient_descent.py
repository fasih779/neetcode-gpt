class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        x=init
        for _ in range(iterations):
            grd=2*x
            x=x-learning_rate*grd
        return round(x,5)


        