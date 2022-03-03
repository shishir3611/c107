import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('csv/data.csv')

mean = df.groupby(['student_id','level'])['attempt'].mean()
print(mean)
fig = px.scatter(mean,x = 'student_id',y = 'level', size = 'attempt', color = 'attempt')

fig.show()