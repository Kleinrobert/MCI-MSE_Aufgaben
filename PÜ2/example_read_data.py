# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array
for i in range(3):
    m = str(i + 1)
    x = ('input_data/power_data_'+m +'.txt')
    power_data_watts = open(x).read().split("\n")
    y = np.array(power_data_watts)
    plt.title("Line graph")
    plt.plot(y, color="blue")
    plt.show()

# Gut, aber eine flexible Zahl an Dateien wäre noch besser -YS 
# %%

# %%

# %%

# %%
