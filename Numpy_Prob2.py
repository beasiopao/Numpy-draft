import numpy as np
X = np.linspace(1,100,100)
X.resize(10,10)
A = np.square(X)
if A%3==0:
    print(A)

np.save('div_by_3', )

    