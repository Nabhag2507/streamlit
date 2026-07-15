# working with input files 

import streamlit as st
import pandas as pd

def c4():
    st.header("Upload your csv file")
    file = st.file_uploader("Choose files", type = ["csv"])

    if file:
        df = pd.read_csv(file)
        st.subheader("Data preview")
        st.dataframe(df)

    if file:
        st.subheader("Stats summary")
        st.write(df.describe())

    if file:
        cities = df["City"].unique()
        selected_city = st.selectbox("Select city ", cities)
        new_df = df[df["City"] == selected_city]

        st.write(new_df)