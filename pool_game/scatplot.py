import pandas as pd
import matplotlib.pyplot as plt
pd = pd.read_csv("/home/johntey/penguins.csv")

x = 1, 2,4,7,9
y=3,4,9,5,8

plt.hist(y, x)
plt.show()