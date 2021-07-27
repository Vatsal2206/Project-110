# Importing modules

import random
import plotly.figure_factory as pff
import statistics as stc
import pandas as pd

#  Reading csv file

df = pd.read_csv('StudentsPerformance.csv')
data = df['math score'].tolist()

# Population mean

pop_mean = stc.mean(data)
print('Population Mean : ',pop_mean)

# Getting random means

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = stc.mean(dataset)
    return mean

# Plotting graph

def make_graph(data):
    data_set = data

    # Sampling Mean
    sampling_mean = stc.mean(data_set)
    print('Sampling Mean : ', sampling_mean)

    graph = pff.create_distplot([data_set], ["Math Scores"], show_hist=False)   
    graph.show()
    
# Repeating this step 1000 times

def repeat():
    list_of_means = []

    for i in range(0,100):
        means = random_set_of_mean(30)
        list_of_means.append(means)

    make_graph(list_of_means)

repeat()