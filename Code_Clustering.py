import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px

df = pd.read_csv("StudentsPerformance.csv")

df.head()
df.describe()

# 3D Визуал

fig = px.scatter_3d(df, x = "writing score", y='math score', z='reading score', color = 'gender')
fig.show()
fig.write_image("3D_plot.png", scale=2.5)
