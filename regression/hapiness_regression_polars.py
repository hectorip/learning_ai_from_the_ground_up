# The same implementations as hapiness_regression
# but using polars instead of pandas

import polars as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_root = "https://github.com/ageron/data/raw/main/"
life_sat_dataset = pd.read_csv(data_root + "/lifesat/lifesat.csv")
X = life_sat_dataset.select("GDP per capita (USD)")  # [["GDP per capita (USD)"]].values
y = life_sat_dataset.select("Life satisfaction")

life_sat_dataset.plot(kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

model = LinearRegression()

model.fit(X, y)

X_new = [[37_655.20]]
print(model.predict(X_new))

