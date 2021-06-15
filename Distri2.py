import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import random
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def randomSetOfMean(counter):
    result=[]
    for i in  range(0,counter):
        randomIndex=random.randint(0,len(data))
        value=data[randomIndex]
        result.append(value)
    papi=statistics.mean(result)
    return papi
    
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=randomSetOfMean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()
