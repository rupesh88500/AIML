import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

iris = load_iris()

print("--- Directory of iris dataset object ---")
print(dir(iris))

print("\n--- Feature Names ---")
print(iris.feature_names)

print("\n--- Target Names ---")
print(iris.target_names)

df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("\n--- DataFrame Head (Features only) ---")
print(df.head())

df['target'] = iris.target
print("\n--- DataFrame Head (With Target Column) ---")
print(df.head())

print("\n--- DataFrame Head (Target == 1) ---")
print(df[df.target == 1].head())

df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])
print("\n--- DataFrame Head (With Flower Name Column) ---")
print(df.head())

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

print("\n--- DataFrame Head (Target == 2) ---")
print(df2.head())

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color="green", marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color="blue", marker='.')
plt.title('Sepal Metrics')

plt.subplot(1, 2, 2)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color="green", marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color="blue", marker='.')
plt.title('Petal Metrics')

plt.tight_layout()
plt.show()

X = df.drop(['target', 'flower_name'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("\n--- Training Set Length ---")
print(len(X_train))

print("\n--- Testing Set Length ---")
print(len(X_test))

model = SVC()
model.fit(X_train, y_train)
print("\n--- Default Model Fit ---")
print(model)

print("\n--- Default Model Score ---")
print(model.score(X_test, y_test))

print("\n--- Default Model Prediction 1 ---")
print(model.predict([[4.8, 3.0, 1.5, 0.3]]))

print("\n--- Default Model Prediction 2 ---")
print(model.predict([[6.5, 3.0, 5.5, 2.0]]))

print("\n--- Default Model Prediction 3 ---")
print(model.predict([[5.5, 2.8, 4.2, 1.3]]))

model_C100 = SVC(C=100)
model_C100.fit(X_train, y_train)
print("\n--- Model C=100 Score ---")
print(model_C100.score(X_test, y_test))

model_C10 = SVC(C=10)
model_C10.fit(X_train, y_train)
print("\n--- Model C=10 Score ---")
print(model_C10.score(X_test, y_test))

model_linear_kernel = SVC(kernel='linear')
model_linear_kernel.fit(X_train, y_train)
print("\n--- Linear Kernel Model Fit ---")
print(model_linear_kernel)

print("\n--- Linear Kernel Model Score ---")
print(model_linear_kernel.score(X_test, y_test))

y_pred = model_linear_kernel.predict(X_test)

print("\n--- Confusion Matrix (Linear Kernel Model) ---")
print(confusion_matrix(y_test, y_pred))

print("\n--- Classification Report (Linear Kernel Model) ---")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
