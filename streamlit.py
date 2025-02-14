import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Variable csv yang sudah dicleaning
freight_value_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/freight_value_products_category.csv');

st.title('Analisis Dataset E-Commerce Public Dataset')

homepageTab, farhanTab, idinTab, ikhsanTab, faishalTab, dwiTab, rizqiTab = st.tabs(['Main Page', 'Product & Payment Type', 'Review Score & Order Status', 'Review Score & Freight value', 'Most Expensive and Most Cheap Product','Cities with the Highest and Lowest Orders', 'Product Average'])


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

with homepageTab:
    st.html(
        "<p style='text-align: center; text-decoration: underline'>Team 5 Pemrograman Dasar Sains Data</p>"
    )
    col1, col2 = st.columns(2);
    col1.image('./our-images/farhanPhoto.jpg', width=250)
    col1.image('./our-images/agiPhoto.jpg', width=250)
    col2.image('./our-images/ikhsanPhoto.jpg', width=250)
    col1.image('./our-images/faishalPhoto.jpg', width=250)
    col2.image('./our-images/idinPhoto.jpg', width=250)
    col2.image('./our-images/rizqiPhoto.jpg', width=250)

with farhanTab: 
    order_products_all_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/order_products_all_df.csv');

    products_all_join = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/products_all_join.csv');

    # Menghitung banyaknya produk yg terjual
    groupby_product = order_products_all_df.groupby('product_category_name_english')['order_item_id'].count().reset_index()

    # Mengurutkan order_item_id secara Descending
    groupby_product = groupby_product.sort_values       (by='order_item_id', ascending=False)

    # Menghitung banyaknya payment_type yang dilakukan dalam membeli barang
    groupby_payment_type = products_all_join.groupby        ('payment_type')['payment_installments'].count().reset_index()

    # Mengurutkan data secara descending
    groupby_payment_type = groupby_payment_type.sort_values     (by='payment_installments', ascending=False)

    # Mengambil 5 sample data
    sample_products = groupby_product.head(5)

    # Bar Chart Pertanyaan 1 : 
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

    
    fig, ax = plt.subplots()
    bars = ax.bar(x, y, color=colors)
    addNumbers(bars)

    ax.set_title('Produk dengan Pembelian Tertinggi')
    ax.set_xlabel('Produk')
    ax.set_ylabel('Jumlah Beli')
    plt.xticks(rotation=30)
    st.pyplot(fig)

    # Bar Chart Pertanyaan 2 : 
    # Mendefinisikan sumbu x dan y serta colornya
    colors = [
        '#0E98BA',
        '#0E98BA', '#0E98BA',
        'lightblue', 'lightblue',
        'lightblue', 'lightblue',
        'lightblue', 'lightblue',
        'lightblue']
    
    fig1, ax1 = plt.subplots()
    bars = ax1.bar(x, y, color=colors)
    addNumbers(bars)

    ax1.set_title('3 Produk dengan Pembelian Tertinggi')
    ax1.set_xlabel('Produk')
    ax1.set_ylabel('Jumlah Beli')
    plt.xticks(rotation=30)
    st.pyplot(fig1)

    # Pie chart
    fig2, ax2 = plt.subplots(figsize=(6, 6))  # Set ukuran figure
    selected_payment_type = groupby_payment_type.head(4)

    explode = (0.1, 0, 0, 0)  # Memisahkan potongan pertama
    ax2.pie(
        selected_payment_type['payment_installments'],
        explode=explode,
        labels=selected_payment_type['payment_type'].unique(),
        autopct='%1.1f%%',
        shadow=True,
    )
    ax2.set_title('Persentase Payment Type yang Digunakan')  # Set judul pie chart
    st.pyplot(fig2)  # Tampilkan pie chart


with idinTab:
    product_translated_not_null = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/order_products_all_df.csv')
    reviews_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/reviews_products_category.csv')
    orders_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/orders_df.csv')
    

    # filter data review_score yang bernilai 1 sampai 5
    low_score_products_1 = reviews_products_category[reviews_products_category["review_score"] == 1]
    low_score_products_2 = reviews_products_category[reviews_products_category["review_score"] == 2]
    low_score_products_3 = reviews_products_category[reviews_products_category["review_score"] == 3]
    low_score_products_4 = reviews_products_category[reviews_products_category["review_score"] == 4]
    low_score_products_5 = reviews_products_category[reviews_products_category["review_score"] == 5]

    # menghitung jumlah produk bernilai 1 sampai 5
    product_count_1 = low_score_products_1["product_id"].nunique()
    product_count_2 = low_score_products_2["product_id"].nunique()
    product_count_3 = low_score_products_3["product_id"].nunique()
    product_count_4 = low_score_products_4["product_id"].nunique()
    product_count_5 = low_score_products_5["product_id"].nunique()

    # filter data order_status
    order_status_1 = orders_df[orders_df["order_status"] == "delivered"]
    order_status_2 = orders_df[orders_df["order_status"] == "shipped"]
    order_status_3 = orders_df[orders_df["order_status"] == "canceled"]
    order_status_4 = orders_df[orders_df["order_status"] == "unavailable"]
    order_status_5 = orders_df[orders_df["order_status"] == "created"]
    order_status_6 = orders_df[orders_df["order_status"] == "invoiced"]
    order_status_7 = orders_df[orders_df["order_status"] == "processing"]
    order_status_8 = orders_df[orders_df["order_status"] == "approved"]

    # menghitung jumlah tiap order_status
    order_status_count_1 = order_status_1["order_id"].nunique()
    order_status_count_2 = order_status_2["order_id"].nunique()
    order_status_count_3 = order_status_3["order_id"].nunique()
    order_status_count_4 = order_status_4["order_id"].nunique()
    order_status_count_5 = order_status_5["order_id"].nunique()
    order_status_count_6 = order_status_6["order_id"].nunique()
    order_status_count_7 = order_status_7["order_id"].nunique()
    order_status_count_8 = order_status_8["order_id"].nunique()

    # Soal nomor 1
    # Menghitung distribusi review_score
    review_score_counts = reviews_products_category["review_score"].value_counts()

    # Total review
    total_reviews = review_score_counts.sum()

    # Persentase review untuk setiap skor
    review_score_percentages = (review_score_counts / total_reviews) * 100

    # Pie chart
    labels = review_score_counts.index  # Skor review (1, 2, 3, 4, 5)
    sizes = review_score_percentages   # Persentase untuk setiap skor
    colors = ['red', 'orange', 'yellow', 'green', 'blue']  # Warna untuk setiap skor
    explode = [0.1 if score == 1 else 0 for score in labels]  # Membedakan slice untuk skor 1

    fig, ax = plt.subplots(figsize=(8, 8))

    # Membuat pie chart
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True
    )
    plt.title("Review Score yang bernilai 1 dalam Persentase")
    st.pyplot(fig)


    # Data untuk horizontal bar chart
    status_labels = [
        "delivered", "shipped", "canceled",
        "unavailable", "created", "invoiced",
        "processing", "approved"
    ]

    status_counts = [
        order_status_count_1, order_status_count_2, order_status_count_3,
        order_status_count_4, order_status_count_5, order_status_count_6,
        order_status_count_7, order_status_count_8
    ]

    # Menghitung total dan persentase
    total_orders = sum(status_counts)
    status_percentages = [(count / total_orders) * 100 for count in status_counts]

    # Membuat horizontal bar chart
    fig1, ax1 = plt.subplots(figsize=(10, 6))

    ax1.barh(status_labels, status_percentages, color=plt.cm.Paired.colors)

    # Menambahkan judul dan label
    ax1.set_title("Persentase Order Berdasarkan Status", fontsize=14)
    ax1.set_xlabel("Persentase (%)", fontsize=12)
    ax1.set_ylabel("Order Status", fontsize=12)

    # Menambahkan nilai persentase pada bar
    for i, v in enumerate(status_percentages):
        ax1.text(v + 0.5, i, f"{v:.1f}%", fontsize=10, va='center')

    # Menampilkan grid pada sumbu x
    ax1.grid(axis='x', linestyle='--', alpha=0.7)

    # Menampilkan plot
    # plt.tight_layout()
    st.pyplot(fig1)

    st.text('')

with ikhsanTab:
    items_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/items_products_category.csv')
    items_sellers = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/items_sellers.csv')
    freight_value_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/freight_value_products_category.csv')
    reviews_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/reviews_products_category.csv')
    freight_value_per_city = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/freight_value_per_city.csv')

    #nomor 1
    # filter data review_score yang bernilai 1 sampai 5
    low_score_products_1 = reviews_products_category[reviews_products_category["review_score"] == 1]
    low_score_products_2 = reviews_products_category[reviews_products_category["review_score"] == 2]
    low_score_products_3 = reviews_products_category[reviews_products_category["review_score"] == 3]
    low_score_products_4 = reviews_products_category[reviews_products_category["review_score"] == 4]
    low_score_products_5 = reviews_products_category[reviews_products_category["review_score"] == 5]

    # menghitung jumlah produk bernilai 1 sampai 5
    product_count_1 = low_score_products_1["product_id"].nunique()
    product_count_2 = low_score_products_2["product_id"].nunique()
    product_count_3 = low_score_products_3["product_id"].nunique()
    product_count_4 = low_score_products_4["product_id"].nunique()
    product_count_5 = low_score_products_5["product_id"].nunique()

    #Bar Chart nomor 1
    # Data dari hasil perhitungan
    scores = [1, 2, 3, 4, 5]
    product_counts = [product_count_1, product_count_2, product_count_3, product_count_4, product_count_5]

    # Pewarnaan khusus untuk review_score = 5
    colors = ['grey', 'grey', 'grey', 'grey', 'orange']  # Warna berbeda untuk score 5

    # Membuat barchart
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.bar(scores, product_counts, color=colors, edgecolor="black")

    # Menambahkan detail ke grafik
    ax1.set_title("Distribusi Jumlah Produk Berdasarkan Review Score Yang Bernilai 5(orange)", fontsize=14)
    ax1.set_xlabel("Review Score", fontsize=12)
    ax1.set_ylabel("Jumlah Produk", fontsize=12)
    plt.xticks(scores)  # Menampilkan angka 1-5 pada sumbu x
    ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Grid horizontal untuk estetika

    # Menampilkan nilai di atas setiap bar
    for i, count in enumerate(product_counts):
        ax1.text(scores[i], count + 2, str(count), ha='center', fontsize=10)

    # Menampilkan plot
    st.pyplot(fig1)

    #Nomor 2
    # Menghitung total freight_value untuk setiap product_id
    freight_value_per_product = items_products_category.groupby("product_id")["freight_value"].sum().reset_index()  

    # Mengurutkan data berdasarkan freight_value dan mengambil 3 produk teratas
    top_3_freight = freight_value_products_category.sort_values(by="freight_value", ascending=False).head(3)
    
    #Bar chart nomor 2
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.bar(top_3_freight["product_category_name_english"], top_3_freight["freight_value"], color="orange")
    ax2.set_title("Top 3 Produk dengan Freight Value Tertinggi", fontsize=16)
    ax2.set_xlabel("Kategori Produk", fontsize=12)
    ax2.set_ylabel("Total Freight Value", fontsize=12)
    plt.xticks(rotation=45)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)  # Grid horizontal untuk estetika
    plt.tight_layout()

    # Menampilkan plot
    st.pyplot(fig2)

    #nomor 3
    # Menghitung rata-rata freight_value untuk setiap seller_city
    freight_value_per_city = items_sellers.groupby("seller_city")["freight_value"].mean().reset_index()

    # Mengurutkan data berdasarkan rata-rata freight_value secara descending dan mengambil 5 kota teratas
    top_5_cities = freight_value_per_city.sort_values(by="freight_value", ascending=False).head(5)
    top_5_cities_df = top_5_cities

    #Bar chart nomor 3
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.bar(top_5_cities_df["seller_city"], top_5_cities_df["freight_value"], color="blue")
    ax3.set_title("5 Kota dengan Rata-Rata Freight Value Terbesar", fontsize=16)
    ax3.set_xlabel("Kota", fontsize=12)
    ax3.set_ylabel("Rata-Rata Freight Value", fontsize=12)
    plt.xticks(rotation=45)
    ax3.grid(axis='y', linestyle='--', alpha=0.7)  # Grid horizontal untuk estetika
    plt.tight_layout()
    
    # Menampilkan plot
    st.pyplot(fig3)

with faishalTab:
   product_translated_not_null = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/product_translated_not_null.csv')

   max_harga = product_translated_not_null['price'].max()
   final_result_max = product_translated_not_null[product_translated_not_null['price'] == max_harga].head(1)

   min_harga = product_translated_not_null['price'].min()
   final_result_min = product_translated_not_null[product_translated_not_null['price'] == min_harga].head(1)

   # Urutkan data berdasarkan harga (price) secara descending
   productTranslated_no_duplicates_sorted_desc = product_translated_not_null.sort_values(by='price', ascending=False)

   # Ambil 10 data dengan harga tertinggi
   top_10_highest_price = productTranslated_no_duplicates_sorted_desc.head(14)

   # Membuat horizontal bar chart
   fig1, ax1 = plt.subplots(figsize=(12, 6))
   ax1.bar(top_10_highest_price['product_category_name_english'], top_10_highest_price['price'], color='skyblue')

   # Menambahkan label dan judul
   ax1.set_xlabel('Nama Produk', fontsize=12)
   ax1.set_ylabel('Harga Produk', fontsize=12)
   ax1.set_title('Bar Chart 10 Produk dengan Harga Tertinggi', fontsize=14)
   plt.xticks(rotation=90, fontsize=10)
   plt.tight_layout()

   # Tampilkan grafik
   st.pyplot(fig1)

   # Urutkan data berdasarkan harga (price) secara ascending
   productTranslated_no_duplicates_sorted_asc = product_translated_not_null.sort_values(by='price', ascending=True)

   # Ambil 10 data dengan harga terendah
   top_10_lowest_price = productTranslated_no_duplicates_sorted_asc.head(45)

   # Plotting
   fig2, ax2 = plt.subplots(figsize=(12, 6))
   ax2.bar(top_10_lowest_price['product_category_name_english'], top_10_lowest_price['price'], color='skyblue')

   # Menambahkan label dan judul
   ax2.set_xlabel('Nama Produk', fontsize=12)
   ax2.set_ylabel('Harga Produk', fontsize=12)
   ax2.set_title('Bar Chart 10 Produk dengan Harga Terendah', fontsize=14)
   plt.xticks(rotation=90, fontsize=10)
   plt.tight_layout()

   # Tampilkan grafik
   st.pyplot(fig2)

with dwiTab:
   final_df_join = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/final_df_join.csv')

   # Pertanyaan 1
   # Filter data untuk kategori "perfumery"
   parfum_orders = final_df_join[final_df_join['product_category_name_english'].str.lower() == 'perfumery']

   # Hitung jumlah order per kota
   orders_by_city = parfum_orders.groupby('seller_city')['order_id'].count().reset_index()

   # Urutkan kota berdasarkan jumlah order tertinggi
   orders_by_city = orders_by_city.sort_values(by='order_id', ascending=False)

   # Pertanyaan 2
   # Filter data untuk kategori "furniture_decor"
   furniture_orders = final_df_join[final_df_join['product_category_name_english'].str.lower() == 'furniture_decor']

   # Hitung jumlah order per kota
   orders_by_city = furniture_orders.groupby('seller_city')['order_id'].count().reset_index()

   # Urutkan kota berdasarkan jumlah order tertinggi
   orders_by_city = orders_by_city.sort_values(by='order_id', ascending=False)

   # Ambil 10 kota dengan jumlah pesanan tertinggi
   top_10_cities = orders_by_city.head(10)
   
   # Plotting
   fig1, ax1 = plt.subplots(figsize=(12, 6))
   plt.bar(top_10_cities['seller_city'], top_10_cities['order_id'], color='orange')
   
   # Menambahkan judul dan label
   ax1.set_title('10 Kota dengan Pesanan Perfumery Tertinggi', fontsize=16)
   ax1.set_xlabel('Daftar Nama Kota', fontsize=12)
   ax1.set_ylabel('Jumlah Pesanan', fontsize=12)
   plt.xticks(rotation=45)
   
   # Tampilkan grafik
   st.pyplot(fig1)

   # Ambil 10 kota dengan jumlah pesanan tertinggi
   top_10_cities = orders_by_city.head(10)
   
   # Visualisasi
   fig2, ax2 = plt.subplots(figsize=(12, 6))
   plt.bar(top_10_cities['seller_city'], top_10_cities['order_id'], color='green')
   
   # Menambahkan judul dan label
   ax2.set_title('10 Kota dengan Pesanan Furniture Decor Tertinggi', fontsize=16)
   ax2.set_xlabel('Daftar Nama Kota', fontsize=12)
   ax2.set_ylabel('Jumlah Pesanan', fontsize=12)
   plt.xticks(rotation=45)

   # Tampilkan grafik
   st.pyplot(fig2)

with rizqiTab:
   products_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/products_df.csv')

   # Hitung rata-rata dimensi
   products_df['average_dimension'] = (products_df['product_length_cm'] + products_df['product_width_cm'] + products_df['product_height_cm']) / 3

   # Pilih beberapa data untuk visualisasi (misalnya, 10 produk pertama)
   sample_data = products_df[['product_category_name', 'average_dimension']].head(10)

   # Membuat diagram batang
   fig1, ax1 = plt.subplots(figsize=(10, 6))
   plt.bar(sample_data['product_category_name'], sample_data['average_dimension'], color='skyblue')
   ax1.set_xlabel('Product Category Name', fontsize=12)
   ax1.set_ylabel('Average Dimension (cm)', fontsize=12)
   ax1.set_title('Rata Rata Dimensi Product', fontsize=14)
   plt.xticks(rotation=45, ha='right')
   plt.tight_layout()

   st.pyplot(fig1)