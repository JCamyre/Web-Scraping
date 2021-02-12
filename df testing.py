import pandas as pd  

df = pd.DataFrame(data={'ticker': ['NOK', 'AAPL'], 'price': [5, 105]})
# how to access a specific ticker?
print(df[df['ticker'] == 'NOK'])

