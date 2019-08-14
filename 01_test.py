# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

np.random.seed(0)

n = np.random.randint(0,10,10)
series = pd.Series(n, name='los')

series.dtype
series.iloc[4]
series.iloc[-1]
series.name
series.size
series.shape

array_A = series.values

# %%

N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

#%%
series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)
series.drop_duplicates()
series[4] = np.nan
series.dropna()

series.idxmax()
series.count()
series.std()
series.describe()
#%%

hist_data = pd.Series(np.random.randn(1000))
hist_data.hist(bins=80)

top_3 = series.nlargest(3)
bottom_3= series.nsmallest(3)

sorted_data = series.sort_values(ascending=False)
