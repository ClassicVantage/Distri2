import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import random

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
standardDeviation=statistics.stdev(data)
print(population_mean)
print(standardDeviation)

fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()