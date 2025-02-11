import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Variable csv yang sudah dicleaning
final_df_join = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/final_df_join.csv');

freight_value_per_city = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/freight_value_per_city.csv');

freight_value_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/freight_value_products_category.csv');

order_products_all_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/order_products_all_df.csv');

product_translated_not_null = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/product_translated_not_null.csv');

products_all_join = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/products_all_join.csv');

reviews_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/E-Commerce-Public-Dataset/reviews_products_category.csv');


st.title('Analisis Dataset E-Commerce Public Dataset')

tab1, farhanTab, tab3 = st.tabs(['Our Team', 'Product & Payment Type', 'Profit'])

with tab1 :
    file = st.file_uploader('Unggah File', type='csv')
    if file is not None:
        Data = pd.read_csv(file)

        # Tampilkan isi dataframe   
        st.write('Isi dari Dataframe adalah : ')
        st.dataframe(Data)

# Fungsi untuk menampilkan angka pada bar chart
def addNumbers(bars):
  for bar in bars:
    # Mengambil lebar bar chart
    height = bar.get_height()

    # Menambahkan label di ujung bar
    plt.text(
        bar.get_x() + bar.get_width() / 2, # Menampilkan label di tengah bar
        height + 0.1,
        f'{int(height)}',
        ha = 'center',
        va = 'bottom',
        color='black',
    )

with farhanTab: 
    if file is not None:
        # Menghitung banyaknya produk yg terjual
        groupby_product = order_products_all_df.groupby('product_category_name_english')['order_item_id'].count().reset_index()

        groupby_product.head()
        
        # Mengurutkan order_item_id secara Descending
        groupby_product = groupby_product.sort_values       (by='order_item_id', ascending=False)

        # groupby_product[['product_category_name_english', 'or']]
        groupby_product

        # Menghitung banyaknya payment_type yang dilakukan dalam membeli barang
        groupby_payment_type = products_all_join.groupby        ('payment_type')['payment_installments'].count().reset_index        ()

        groupby_payment_type

        # Mengurutkan data secara descending
        groupby_payment_type = groupby_payment_type.sort_values     (by='payment_installments', ascending=False)

        groupby_payment_type

        # Mengambil 5 sample data
        sample_products = groupby_product.head(5)
        sample_products


        # Mendefinisikan sumbu x dan y serta colornya
        colors = [
            '#0E98BA',
            'lightblue', 'lightblue',
            'lightblue', 'lightblue',
            'lightblue', 'lightblue',
            'lightblue', 'lightblue',
            'lightblue']
        x = sample_products['product_category_name_english']
        y = sample_products['order_item_id']


        bars = plt.bar(
            x,
            y,
            color=colors
        )

        addNumbers(bars)

        plt.xlabel('Produk')
        plt.ylabel('Jumlah Beli')
        plt.xticks(rotation=30)
        plt.show()

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