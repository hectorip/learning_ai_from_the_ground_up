import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_root = "https://github.com/ageron/data/raw/main/"
life_sat_dataset = pr.read_csv(data_root + "/lifesat/lifesat.csv")
X = life_sat_dataset[["GDP per capita (USD)"]].values
y = life_sat_dataset[["Life satisfaction"]].values

life_sat_dataset.plot(kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()


