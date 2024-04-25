#Cargamos las librerías necesarias para el análisis exploratorio de los datos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings
#Inicialización de Seaborn
warnings.filterwarnings('ignore')
sns.set(style='white')
df = pd.read_csv('yellow_tripdata_2015-01.csv', nrows=100000)
print(df.shape, df.columns)