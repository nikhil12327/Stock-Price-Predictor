# visualize.py
import matplotlib.pyplot as plt
import pandas as pd
from preprocessing import prepare_features
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../data/aapl_sample.csv')
X, y, dfp = prepare_features(df)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(10,5))
plt.plot(dfp['Date'], y, label='Actual Close Price')
plt.plot(dfp['Date'], y_pred, label='Predicted Close Price')
plt.xticks(rotation=45)
plt.legend()
plt.title('Stock Price: Actual vs Predicted (sample)')
plt.tight_layout()
plt.show()
