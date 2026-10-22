import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

file_path = r"C:\Users\user\Desktop\study\advertising.csv"

data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

X = data[["TV"]]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(10, 6))

plt.scatter(X_test, y_test, color="blue", label="Actual Data (Test Set)")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression Line")

plt.title("Linear Regression: TV Budget vs Sales", fontsize=14)
plt.xlabel("TV Advertising Budget ($1000s)", fontsize=12)
plt.ylabel("Sales (Units)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()
