import streamlit as st


def make_chai():
    st.title("Chai maker app:)")

    add_masala = st.checkbox("Add masala")

    if add_masala:
        st.write("Masala added to your tea.")

    name = st.text_input("Enter your name : ")
    if(name):
        st.write(f"Welcome, {name}")

    dob = st.date_input("Enter your dob")
    if(dob):
        st.write(f"Your dob is {dob}")

    radio_button = st.radio("Choose tea base : ", ["milk", "water", "something"])

    flavour = st.selectbox("Choose your flavour", ["Adarak", "kesar", "tulsi"])

    sugar_level = st.slider("Sugar level", 0, 10, 1)

    cups = st.number_input("How many cups do you want?", min_value = 1, max_value = 10)

    if st.button("Make tea"):
        st.write(f"Selected type is {radio_button}, flavour is {flavour}")
        st.write(f"Total sugar spoon is {sugar_level}")
        st.write(f"Total {cups} cup tea ordered.")
        st.success("Your tea is ready.")
