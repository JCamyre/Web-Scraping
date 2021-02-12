import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

event = pd.read_csv('MLSO 2020 Applicant Event Interests (Responses) - Form Responses 1.csv')
# for column in event.columns[4:]:
# 	print(event[column].value_counts()[:5])
popular_events = [event[column].value_counts()[:5] for column in event.columns[4:]]
print(len(event[event.columns[2]].unique()))
print(popular_events[0])
# print(event[event.columns[4:]])
# Maybe I can go from the series to getting a tuple of the top five from each series, then use that to graph
f, ax = plt.subplots(figsize=(6, 15))
# sns.barplot(x='')

