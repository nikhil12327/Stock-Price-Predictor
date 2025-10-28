# model.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import pandas as pd
from preprocessing import prepare_features

def train_and_save(data_csv='../data/aapl_sample.csv', out_model='../model/stock_model.pkl'):
    df = pd.read_csv(data_csv)
    X, y, dfp = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'MSE: {mse:.4f}, R2: {r2:.4f}')
    joblib.dump(model, out_model)
    print('Saved model to', out_model)

if __name__ == '__main__':
    train_and_save()
