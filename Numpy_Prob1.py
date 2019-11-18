import numpy as np
X = np.random.random((5,5))
Z = (X - X.mean())/(np.std(X))
np.save('X_normalized', Z)