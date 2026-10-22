import pandas as pd
import matplotlib.pyplot as plt

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
visitors = [120, 450, 190, 240, 310]

df = pd.DataFrame({"Visitors": visitors}, index=days)
plt.plot(df.index, df["Visitors"], color="purple", marker="o")
plt.title("Weekly Website Traffic")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Visitors")
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X_data = np.linspace(0, 10, 100)
y_data = 2 * X_data + 1 + np.random.randn(100) * 2

X_fit = np.linspace(0, 10, 100)
y_fit = 2 * X_fit + 1

plt.scatter(X_data, y_data, color='blue')
plt.plot(X_fit, y_fit, color='red')
plt.title('Data Scatter and Trend Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

import numpy as np
import tensorflow as tf

np.random.seed(42)

X_data = np.random.rand(100, 1)
y_data = 2 * X_data + 1 + np.random.randn(100, 1) * 0.1

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')
history = model.fit(X_data, y_data, epochs=50, verbose=0)

for epoch, loss in enumerate(history.history['loss'][::10]):
    print(f"Epoch {epoch*10:02d} Loss: {loss:.4f}")

prediction = model.predict(np.array([[0.5]]))
print(f"\nPrediction for x=0.5: {prediction[0][0]:.4f}")


import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

colors = ['navy', 'turquoise', 'darkorange']

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, label=target_name)

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()
