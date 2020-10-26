import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("bellcurve.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist = False)
fig.show()