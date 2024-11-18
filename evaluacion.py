#['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam', 'ra','dec',  'mag', 'ci', 'rv', "con"]
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor
import pickle as pk

def preparacion(values):
    con = np.array(values[13])
    columns = ['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam', 'ra','dec', 'mag', 'ci', 'rv']
    
    constelations = np.array(['And', 'Ant', 'Aps', 'Aql', 'Aqr', 'Ara', 'Ari', 'Aur', 'Boo', 'CMa',
       'CMi', 'CVn', 'Cae', 'Cam', 'Cap', 'Car', 'Cas', 'Cen', 'Cep', 'Cet',
       'Cha', 'Cir', 'Cnc', 'Col', 'Com', 'CrA', 'CrB', 'Crt', 'Cru', 'Crv',
       'Cyg', 'Del', 'Dor', 'Dra', 'Equ', 'Eri', 'For', 'Gem', 'Gru', 'Her',
       'Hor', 'Hya', 'Hyi', 'Ind', 'LMi', 'Lac', 'Leo', 'Lep', 'Lib', 'Lup',
       'Lyn', 'Lyr', 'Men', 'Mic', 'Mon', 'Mus', 'Nor', 'Oct', 'Oph', 'Ori',
       'Pav', 'Peg', 'Per', 'Phe', 'Pic', 'PsA', 'Psc', 'Pup', 'Pyx', 'Ret',
       'Scl', 'Sco', 'Sct', 'Ser', 'Sex', 'Sge', 'Sgr', 'Tau', 'Tel', 'TrA',
       'Tri', 'Tuc', 'UMa', 'UMi', 'Vel', 'Vir', 'Vol', 'Vul'])
    col = np.where(constelations == con)
    columns = np.concatenate((columns,constelations))
    cons_values = np.array([0 for _ in range(len(constelations))])
   
    cons_values[col] = 1
    values  = np.delete(values,13)
    values = np.concatenate((values,cons_values))
    
  
    values = [values]
    x_data = pd.DataFrame(columns=columns, data=values)
    return(x_data)
#values = [True,True,False,True,True,False,False,False,1.5,50,2,1.4,10,"Sex"]
#x_data = preparacion(values)

def prediccion(x_data):
    with open(file_name, 'rb') as f:
        loaded_model = pickle.load(f)
    dist = modelo_escogido.predict(x_data)
    return(dist)
#print(prediccion(x_data))
