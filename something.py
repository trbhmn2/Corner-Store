import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql.cursors
import datetime 
from difflib import SequenceMatcher
sns.set(rc={'figure.figsize':(10,5)})

lis = []
lis2= []

try:
    conn = pymysql.connect(
        host='learningcomputerscience.com', port=3306, user='test_remote', 
        password='test_remote!', database='9_8_BT', charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipt")
    results = cursor.fetchall()
    for result in results:
        lis.append(result)
    total = pd.DataFrame.from_dict(lis)

    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    for result in results:
        lis2.append(result)
    items = pd.DataFrame.from_dict(lis2)
    items = items.set_index("name")

except Exception as e:
    st.error(f"Database connection failed: {e}")

if not items.empty:
    IDn = items['id'].max() + 1
else:
    IDn = 1

with st.sidebar:
    add_item = st.button("Would you like to add a new item?")
    if add_item:
        with st.form("my_form"):
            add_type = st.radio(
                "Choose the type of product it would be...",
                ("Snack", "Drink", "Utility"))
            typ = add_type.lower() + 's'
            st.write(IDn)
            add_name = st.text_input("", "Name of product?")
            add_og_price = st.text_input("", "Price of product?")
            add_price_sold = st.text_input("", "Price sold of product?")
            sent = st.form_submit_button("Publish/Send off")
            if sent:
                try:
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO items (name, id, price_sold, type, og_price) VALUES (%s, %s, %s, %s, %s)", 
                        (add_name, IDn, add_price_sold, typ, add_og_price))
                    conn.commit()
                    cursor.close()
                    conn.close()
                except Exception as e:
                    st.error(f"Failed to add item: {e}")

total['quantity_bought'] = total['quantity_bought'].replace(0, 1)
total['revenue'] = total.apply(
    lambda row: items.at[row['item'], 'price_sold'] if row['revenue'] == 0 and row['item'] in items.index else row['revenue'], axis=1
)

total['profit'] = total.apply(
    lambda row: ((row['revenue'] * row['quantity_bought']) - (items.at[row['item'], 'og_price'] * row['quantity_bought']))
    if row['item'] in items.index else 0,
    axis=1
)

itemxprofit = items.copy()
itemxprofit['profit'] = 0
itemxprofit['revenue'] = 0
itemxprofit['bought'] = 0

for i, row in total.iterrows():
    name = row['item']
    if name in itemxprofit.index:
        itemxprofit.at[name, 'profit'] += row['profit']
        itemxprofit.at[name, 'revenue'] += row['revenue'] * row['quantity_bought']
        itemxprofit.at[name, 'bought'] += row['quantity_bought']

missing_names = total[~total['item'].isin(itemxprofit.index)]['item'].unique()
if len(missing_names) > 0:
    st.warning(f"The following items are missing from the item list: {missing_names}")

totalrev = total['revenue'].sum()
totalprofit = total['profit'].sum()

st.markdown("<h1 style='text-align: center; color: red;'>Data Analysis</h1>", unsafe_allow_html=True)
st.write('This is a web app to explore purchasing data, and see some visual data of the processes.')

st.write('total revenue ===', totalrev)
st.write('total profit ===', totalprofit)

try:
    cursor.close()
    conn.close()
except:
    pass