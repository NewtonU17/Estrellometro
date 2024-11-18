import streamlit as st
import pandas as pd
import numpy as np
import evaluacion


st.title('Estrellometro')
#['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam', 'ra','dec',  'mag', 'ci', 'rv', "con"]
col1, col2= st.columns([1,1])

with col1:
    catalog = st.multiselect(
    "¿En qué catalogos se encuentra la estrella?",
    ('tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam'),
)
    constel = np.array([0,0,0,0,0,0,0,0])
    catag = np.array(['tyc', 'gaia', 'hyg', 'hip', 'hd', 'hr', 'gl', 'flam'])
    for cons in catalog:
        num = np.where(catag == cons)
        constel[num] = 1
        
    con = st.selectbox("¿En que constelación esta la estrella?",('And', 'Ant', 'Aps', 'Aql', 'Aqr', 'Ara', 'Ari', 'Aur', 'Boo', 'CMa',
       'CMi', 'CVn', 'Cae', 'Cam', 'Cap', 'Car', 'Cas', 'Cen', 'Cep', 'Cet',
       'Cha', 'Cir', 'Cnc', 'Col', 'Com', 'CrA', 'CrB', 'Crt', 'Cru', 'Crv',
       'Cyg', 'Del', 'Dor', 'Dra', 'Equ', 'Eri', 'For', 'Gem', 'Gru', 'Her',
       'Hor', 'Hya', 'Hyi', 'Ind', 'LMi', 'Lac', 'Leo', 'Lep', 'Lib', 'Lup',
       'Lyn', 'Lyr', 'Men', 'Mic', 'Mon', 'Mus', 'Nor', 'Oct', 'Oph', 'Ori',
       'Pav', 'Peg', 'Per', 'Phe', 'Pic', 'PsA', 'Psc', 'Pup', 'Pyx', 'Ret',
       'Scl', 'Sco', 'Sct', 'Ser', 'Sex', 'Sge', 'Sgr', 'Tau', 'Tel', 'TrA',
       'Tri', 'Tuc', 'UMa', 'UMi', 'Vel', 'Vir', 'Vol', 'Vul'))

with col2:
    ra = st.number_input(f'Ingrese el número de ascención recta', min_value=0, max_value=30, value=10)
    dec = st.number_input(f'Ingrese el número de declinación', min_value=-90, max_value=90, value=10)
    mag = st.number_input(f'Ingrese el número de magnitud relativa', min_value=0, max_value=10, value=2)
    ci = st.number_input(f'Ingrese el número de indice de color', min_value=-3, max_value=5, value=1)
    rv = st.number_input(f'Ingrese el número de velocidad radial', min_value=-50, max_value=50, value=10)

values = np.concatenate((constel,[ra,dec,mag,ci,rv,con]))
values = evaluacion.preparacion(values)
dist = evaluacion.prediccion(values)

st.write(f"La estrella introducida se encuentra a una distancia de {dist} parsecs según el modelo")