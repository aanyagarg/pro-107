import pandas as pd
import plotly.express as pe
import csv

a = pd.read_csv("data.csv")

mean = a.groupby(["student_id" , "level"], as_index = False)["attempt"].mean()

graph =  pe.scatter(mean , x="student_id" , y="level" , size = "attempt" , color = "attempt" )

graph.show()



