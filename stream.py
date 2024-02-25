import pandas as pd 
import streamlit as st 
import io 
import matplotlib.pyplot as plt 
 
st.title("Интерактивный дашборд") 
 
uploaded_file = st.sidebar.file_uploader("Загрузите файл CSV", type="csv") 
if uploaded_file is not None: 
 
    df = pd.read_csv(uploaded_file) 
else: 
    st.sidebar.warning("Загрузите файл CSV") 
 
if 'df' in locals(): 
 
    unique_months = df['month'].apply(lambda x: x[-2:]).drop_duplicates().tolist() 
 
    years = [int(month.split('-')[0]) for month in df['month']] 
    selected_year = st.sidebar.selectbox("Выберите год",  options=range(min(years), max(years)+1), index=0) 
 
    # Фильтрация данных 
    filtered_data  = df[pd.to_datetime(df['month']).dt.year == selected_year] 
 
    st.subheader("Распределение проверенного оружия по штатам за {}".format(selected_year)) 
    top_states = filtered_data.groupby('state')['totals'].sum().nlargest(10) 
 
 
    fig, ax = plt.subplots(figsize=(10, 8)) 
    top_states.plot.pie(autopct='%1.1f%%', ax=ax) 
    ax.set_ylabel('') 
    st.pyplot(fig)