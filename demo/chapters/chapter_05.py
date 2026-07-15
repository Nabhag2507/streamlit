# sending request in web api (currency converter)

import streamlit as st
import requests


def c5():
    st.title("Live currency converter.")

    url = "https://api.exchangerate-api.com/v4/latest/INR"
    st.write("Enter base currency and amount.")

    response = requests.get(url)
    data = response.json()
    curr_list = data["rates"]

    col1, col2 = st.columns([2, 1])
    with col1:
        base_currency = st.selectbox("Currency", curr_list)
        base_currency_value = data["rates"][base_currency]

    with col2:
        amount = st.number_input("Amount", min_value=0.0, value=1500.0, step=1.0)

    st.write("Enter currency in which you want to convert")
    dest_curr = st.selectbox("", curr_list)

    if st.button("Convert"):

        if response.status_code == 200:

            curr_inr = amount / base_currency_value
            final_curr = curr_inr * data["rates"][dest_curr]

            st.success(f"{amount} {base_currency} = {final_curr:.2f} {dest_curr}")

        else:
            st.error("Failed to convert")
