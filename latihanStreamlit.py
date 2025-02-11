import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Analisis Sample Superstore Data')

tab1, tab2, tab3 = st.tabs(['Unggah File', 'Analisis Data', 'Profit'])
with tab1 :
    file = st.file_uploader('Unggah File', type='csv')
    if file is not None:
        Data = pd.read_csv(file)

        # Tampilkan isi dataframe   
        st.write('Isi dari Dataframe adalah : ')
        st.dataframe(Data)

with tab2: 
    if file is not None:
        # Data = pd.read_csv(file)
        # Mengubah tipe data
        Data['Order Date'] = pd.to_datetime(Data['Order Date'])
        
        # Tambah attribute 
        Data['Month'] = Data['Order Date'].dt.month
        Data['Year'] = Data['Order Date'].dt.year

        # Filter Data Tahun 2015
        Data_2015 = Data[Data['Year'] == 2015]
        Data_2015

        # Statistika Transaksi
        transaksi_per_bulan = Data_2015.groupby('Month')['Sales'].count().sort_index()
        transaksi_per_bulan

        # Grafik
        bulan_list = transaksi_per_bulan.index.tolist()
        jml_transaksi = transaksi_per_bulan.values.tolist()

        fig, ax = plt.subplots()
        ax.bar(
        bulan_list,
        jml_transaksi
        )
        ax.set_xlabel('Jumlah Transaksi Per Bulan Selama Tahun 2015')
        ax.set_ylabel('Bulan')
        ax.set_title('Jumlah Transaksi')
        st.pyplot(fig)

with tab3: 
    if file is not None:
        Kategori_Profit = Data.groupby('Category')['Profit'].sum().sort_values()
        Kategori_Profit

        Kategori_List = Kategori_Profit.index.tolist()
        Profit_List = Kategori_Profit.values.tolist()

        fig, ax = plt.subplots()
        ax.pie(
            Profit_List,
            labels = Kategori_List,
            autopct = '%1.1f%%'
        )

        ax.set_title('Profit Berdasarkan Kategori Produk')
        st.pyplot(fig)