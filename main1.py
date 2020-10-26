import plotly.figure_factory as ff
import pandas as pd
import csv
df  = pd.read_csv("bellcurve.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist = False)
fig.show()