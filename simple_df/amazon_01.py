# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#%%

d = pd.read_clipboard()
columns = [x for x in d.columns]
d_raw =d.drop(["Czas", "1r 3m"], axis=1)
df = pd.DataFrame(d_raw)
#%%

df['Wolumen'] = df["Wolumen"].apply(lambda x: x.replace(" ","")).\
                              apply(lambda x: int(x))
                              
df['Obrót'] = df["Obrót"].apply(lambda x: x.replace(" ","")).\
                          apply(lambda x: int(x))       
                          
df['Udział'] = df["Udział"].apply(lambda x: x.replace("%","")).\
                            apply(lambda x: float(x)) 

#%%
df["Zmiana %"] = df["Zmiana %"].apply(lambda x: x.replace("(","")).\
                                apply(lambda x: x.replace(")","")).\
                                apply(lambda x: x.replace("%","")).\
                                apply(lambda x: x.replace("%","")).\
                                apply(lambda x: float(x))
                                
                                #%%
df["Profil"] = df["Profil"].apply(lambda x: x[0:4])

                                
#%%
k = df.plot(x ="Profil", y="Zmiana %", kind = "bar", color= "blue", 
            title= "Zmiana %", figsize =(5,5))
k.set_xlabel("Nazwa spółki")
