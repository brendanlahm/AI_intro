####################################### Machine Learning Practice
####################### Quick Test
def print_pattern(n):
    if n > 9:
        return
    for i in range(1, n + 1):
        print(i)

n = input("give a number: \n")
n = int(n)
print_pattern(n)

####################### Linear Regression
import numpy as np

class LinearRegression:
    def __init__(self) -> None:
        self.w = np.zeros((2,))

    def fit(self, data, epochs, lr=0.1):
        for epoch in range(epochs):
            pass


reg = LinearRegression()
data = np.array([[1, 1], [2, 3], [4, 3]])
reg.fit(data, 1, lr=0.1)


