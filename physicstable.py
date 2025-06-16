#This was all made with Jupyter Notebook but I just copied the Python code directly from Visual Studio. The Jupyter Notebook language looks very different from Python.

#For calculating centripetal acceleration.
import pandas as pd
import matplotlib.pyplot as plt

df = {'velocity (m/s)': [9, 2, 8],
     'radius (m)': [5, 7, 9]}

table = pd.DataFrame(df, columns = ['velocity (m/s)', 'radius (m)'])

table['centripetal acceleration (m/s^2)'] = (table['velocity (m/s)']) ** 2 / table['radius (m)']

table

#For calculating kinetic energy.
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.plot(df['velocity (m/s)'], df['radius (m)'])
plt.show()

import pandas as pd

df = {'mass (kg)': [9, 2, 8],
     'velocity (m/s)': [5, 7, 9]}

table = pd.DataFrame(df, columns = ['mass (kg)', 'velocity (m/s)'])

table['kinetic energy (J) '] = table['mass (kg)'] * (table['velocity (m/s)']) ** 2

table

