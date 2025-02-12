import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Variable csv yang sudah dicleaning
freight_value_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/freight_value_products_category.csv');

st.title('Analisis Dataset E-Commerce Public Dataset')

farhanTab,idinTab,ikhsanTab= st.tabs(['Product & Payment Type', 'Review Score & Order Status', 'Review Score & Freight_value'])


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
    order_products_all_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/order_products_all_df.csv');

    products_all_join = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/products_all_join.csv');

    # Menghitung banyaknya produk yg terjual
    groupby_product = order_products_all_df.groupby('product_category_name_english')['order_item_id'].count().reset_index()

    # Mengurutkan order_item_id secara Descending
    groupby_product = groupby_product.sort_values       (by='order_item_id', ascending=False)

    # groupby_product[['product_category/_name_english', 'or']]


    # Menghitung banyaknya payment_type yang dilakukan dalam membeli barang
    groupby_payment_type = products_all_join.groupby        ('payment_type')['payment_installments'].count().reset_index()


    # Mengurutkan data secara descending
    groupby_payment_type = groupby_payment_type.sort_values     (by='payment_installments', ascending=False)


    # Mengambil 5 sample data
    sample_products = groupby_product.head(5)

    # Bar Chart Pertanyaan 1
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

    ax.set_xlabel('Produk')
    ax.set_ylabel('Jumlah Beli')
    plt.xticks(rotation=30)
    st.pyplot(fig)

    # Bar Chart Pertanyaan 2
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

with ikhsanTab:
    product_translated_not_null = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/order_products_all_df.csv')
    reviews_products_category = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/reviews_products_category.csv')
    orders_df = pd.read_csv('https://raw.githubusercontent.com/idin132/PDSD/refs/heads/master/main-data/orders_df.csv')
    