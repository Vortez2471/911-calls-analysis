import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_csv('911.csv')

print(df.info())
print('\n\n')

print(df.head(5))
print('\n\n')

var=df['zip'].value_counts().head(5)
print(var)
print('\n\n')

var=df['twp'].value_counts().head(5)
print(var)
print('\n\n')

var=df['title'].nunique()
print(var)
print('\n\n')

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts())
print('\n\n')

sns.countplot(x='Reason',data=df,palette='viridis')

plt.show()

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# It is missing some months! 9,10, and 11 are not there.

byMonth = df.groupby('Month').count()
print(byMonth.head())
print('\n\n')

byMonth['twp'].plot()
plt.show()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()

df['Date']=df['timeStamp'].apply(lambda t: t.date())
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.show()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
plt.show()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
plt.show()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
print(dayHour.head())
print('\n\n')

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')
sns.clustermap(dayHour,cmap='viridis')
plt.plot()

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
print(dayMonth.head())
print('\n\n')

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')
sns.clustermap(dayMonth,cmap='viridis')
plt.show()