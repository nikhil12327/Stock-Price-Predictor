# preprocessing.py
import pandas as pd

def prepare_features(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df = df.dropna().reset_index(drop=True)
    X = df[['Open','High','Low','Volume','MA10','MA50']]
    y = df['Close']
    return X, y, df

if __name__ == '__main__':
    df = pd.read_csv('../data/aapl_sample.csv')
    X,y,df2 = prepare_features(df)
    print('Prepared', len(df2), 'rows with features.')
