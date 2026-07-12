import streamlit as st


def c3():
    name = st.sidebar.text_input("Enter your name")
    chai = st.sidebar.selectbox("Enter your chai", ["Masala", "adarak", "kesar"])

    st.title("Chai taste poll.")
    c1, c2 = st.columns(2)

    with c1:
        vote1 = st.button("Masala chai")
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRhKV9yboxeyEl5KdOTwWeOfNzcCZD8ePW5uJibAZbJQ&s=10",
            width=200,
        )

    with c2:
        vote2 = st.button("Adarak chai")
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHPxtTM_whu7JvFGnsxpfFTw2CgLnRa4HUeRGMK2pAZA&s=10",
            width=200,
        )

    if vote1:
        st.success("Thanks for voting masala chai")

    elif vote2:
        st.success("Thanks for voting adarak chai")

    if st.sidebar.button("Order"):
        st.write(f"Welcome {name}, your {chai} chai is getting ready.")

    with st.expander("Show chain making instructions"):
        st.write("""
            1. Boil water with tea leaves
            2. Add milk and sugar
            3. serve tea
        """)

    st.markdown("> blockquote")
    st.markdown("# heading 1")
    st.markdown("## heading 2")
    st.markdown("### heading 3")