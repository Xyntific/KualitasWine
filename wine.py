import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('wine.sav', 'rb'))
st.title('Klasifikasi Kualitas Wine')
col1, col2 = st.columns(2)

with col1:
    FixedAcidity =st.number_input("Jumlah keasaman tetap")
    VolatileAcidity = st.number_input("Jumlah Keasaman yang mudah menguap")
    CitricAcid = st.number_input("Kadar asam sitrat")
    ResidualSugar = st.number_input("Jumlah gula yang tersisa setelah fermentasi ")
    Chlorides =st.number_input("Kadar Garam")
    FreeSulfurDioxide = st.number_input("Jumlah sulfur dioksida yang bebas")
    

with col2:
    TotalSulfurDioxide = st.number_input("Total sulfur dioksida")
    Density = st.number_input("Jumlah massa per unit volume anggur")
    pH      = st.number_input("Kadar pH")
    sulphates   = st.number_input("Kadar Sulfat")
    alcohol     = st.number_input("Jumlah Kadar Alcohol")



predict = ''
if st.button('Hasil Prediksi'):
    predict = model.predict([[FixedAcidity,VolatileAcidity,CitricAcid,ResidualSugar,Chlorides,FreeSulfurDioxide,TotalSulfurDioxide,Density,pH,sulphates,alcohol,]])

    if(predict[0] == 1):
        predict = 'Wine Berkualitas Baik'
    else:
        predict = 'Wine Berkualitas Buruk'
st.success(predict)
