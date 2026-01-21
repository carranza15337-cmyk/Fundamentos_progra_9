import streamlit as st
import pandas as pd
import numpy as np

st.title("App de Streamlit")
st.header("Este es un encabezado")
st.subheader("Este es un subencabezado")
st.write("Este es un parrafo")
st.write("Este es un segundo parrafo")
st.write("Este es un tercer parrafo")

"___________________________________________"

df = pd.DataFrame(np.random.randn(10, 2), columns=['Precio', 'Ventas'])
st.line_chart(df)
st.dataframe(df)

