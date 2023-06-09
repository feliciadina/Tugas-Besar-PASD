import streamlit as st
import pandas as pd

def main():
    st.title("Web App Video Game Sales")
    st.write("Welcome to Web App Video Game Sales!")

    st.text("Berikut merupakan dataset penjualan video game")

    st.header("Data")
    df = pd.read_csv("pasdjaya.csv")
    st.dataframe(df)

    st.header("Grafik")
    sales_x = st.selectbox("Pilih wilayah penjualan (X)", ["North America (NA)", "Europe (EU)", "Japan (JP)", "Other", "Global"], key='sales_x')
    sales_y = st.selectbox("Pilih wilayah penjualan (Y)", ["North America (NA)", "Europe (EU)", "Japan (JP)", "Other", "Global"], key='sales_y')
   
    # Contoh DataFrame
    df = pd.DataFrame({
        "North America (NA)": [100, 200, 150],
        "Europe (EU)": [50, 75, 80],
        "Japan (JP)": [80, 100, 120],
        "Other": [60, 90, 70],  
        "Global": [120, 180, 150]
    })

    if sales_x in df.columns and sales_y in df.columns:
        st.write("Anda memilih wilayah penjualan (X):", sales_x)
        st.write("Anda memilih wilayah penjualan (Y):", sales_y)

        st.write(f"Visualisasi Wilayah Penjualan {sales_x} dengan {sales_y}")
        st.line_chart(df[[sales_x, sales_y]])
    else:
        st.write("Nama kolom tidak valid")

if __name__ == '__main__':
    main()
