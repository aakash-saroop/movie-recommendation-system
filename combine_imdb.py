import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/aakashsaroop/Desktop/imdb4000.csv')
df2 = pd.read_csv('/Users/aakashsaroop/Desktop/imdb17000.csv')
df3 = pd.read_csv('/Users/aakashsaroop/Desktop/imdb.csv')

df1 = df1.to_numpy()
df2 = df2.to_numpy()
df3 = df3.to_numpy()


entire_data = np.zeros((17434,3))
entire_data[0][0] = 1
entire_data[0][1] = 7.7
entire_data[0][2] = 438

entire_data[1:4001,:] = df1[:4000, :]


entire_data[4001:17001 , :] = df2[4000:17000,:]
entire_data[17001:, :] = df3[17000:,:]
average_no_users = 0
average_rating = 0
for x in range(entire_data.shape[0]):
    average_rating+=entire_data[x][1]/17434
    average_no_users+=entire_data[x][2]/17434
#colors = (0,0,0)
#area = np.pi*3
plt.scatter(entire_data[:,1], entire_data[:,2])
plt.show()
print("Average no. of users", average_no_users)
print("Average rating", average_rating)
