import pandas as pd
data = pd.read_csv('C:/Users/sanch/Downloads/genre_4_35.csv')
data1 = data.iloc[:35,1:].values
import matplotlib.pyplot as plt
plt.plot(data1[:,0], data1[:,1])
plt.show()
