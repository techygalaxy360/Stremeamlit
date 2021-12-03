import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
st.title("Ventiladores Mecanicos")

ven=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores.csv")

st.dataframe(ven)

ventiladores=st.multiselect("Ventiladores", ven.Ventiladores)
st.markdown('Su seleccion es: ' + ' , '.join(ventiladores))

primerafecha=datetime.strptime(ven.columns[15], '%Y-%m-%d')

ultimafecha=datetime.strptime(ven.columns[-1], '%Y-%m-%d')

start_time= st.slider("Seleccione las fechas: ", value=[primerafecha,ultimafecha],format="YYYY-MM-DD")

index_of_primera_fecha=ven.columns.get_loc(start_time[0].strftime('%Y-%m-%d'))
index_of_ultima_fecha=ven.columns.get_loc(start_time[1].strftime('%Y-%m-%d'))

fig,ax=plt.subplots()

ocupados=ven[ven.Ventiladores=='ocupados'] if 'ocupados' in ventiladores else None 
disponible=ven[ven.Ventiladores=='disponibles'] if 'disponibles' in ventiladores else None 
total=ven[ven.Ventiladores=='total'] if 'total' in ventiladores else None 

if (ocupados is not None
    or disponible is not None
    or total is not None):
    superfiltro=pd.concat([ocupados, disponible, total])
    to_plot=superfiltro.iloc[:,index_of_primera_fecha:index_of_ultima_fecha+1]
    ax.plot(to_plot.T)
    ax.set_title(ventiladores)
    ax.set_xlabel("Fechas")
    ax.set_ylabel(ventiladores)
    xs= np.arange(0,index_of_ultima_fecha-index_of_primera_fecha+1)
    plt.xticks(xs,rotation=90)
    st.pyplot(fig)
