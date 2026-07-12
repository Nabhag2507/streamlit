import streamlit as st


def first_demo():
    st.title("First app")
    st.subheader("Build with streamlit.")
    st.text("This is my first demo app")
    st.write("First app description...........")

    drop_down_options = st.selectbox("Select options", ["first", "second", "third"])

    st.write(f"Your choice is {drop_down_options}, excellent choice.")
    st.success("Your choice is selected successfully.")
