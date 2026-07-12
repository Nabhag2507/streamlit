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