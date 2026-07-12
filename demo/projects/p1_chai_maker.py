import time
import streamlit as st

# st.set_page_config(
#     page_title="☕ Chai Maker",
#     page_icon="☕",
#     layout="centered"
# )

def make_chai():
    # ------------------ Sidebar ------------------

    st.sidebar.title("☕ Chai Maker")
    st.sidebar.write("Customize your perfect chai!")

    theme = st.sidebar.selectbox(
        "Choose Theme",
        ["Classic", "Royal", "Healthy"]
    )

    st.sidebar.markdown("---")
    st.sidebar.info("Made with ❤️ using Streamlit")

    # ------------------ Main ------------------

    st.title("☕ Ultimate Chai Maker")
    st.write("Create your own personalized cup of tea!")

    with st.form("chai_form"):

        st.subheader("👤 Customer Details")

        name = st.text_input("Your Name")

        age = st.number_input(
            "Age",
            min_value=5,
            max_value=100,
            value=18
        )

        st.subheader("🥛 Tea Base")

        tea_base = st.radio(
            "Select Tea Base",
            ["Milk", "Water", "Half Milk Half Water"]
        )

        st.subheader("🌿 Flavor")

        flavors = st.multiselect(
            "Select Flavors",
            [
                "Masala",
                "Ginger",
                "Tulsi",
                "Cardamom",
                "Mint",
                "Saffron"
            ]
        )

        sugar = st.slider(
            "Sugar (spoons)",
            0,
            10,
            2
        )

        strength = st.select_slider(
            "Tea Strength",
            options=["Light", "Medium", "Strong"]
        )

        cups = st.number_input(
            "Number of Cups",
            min_value=1,
            max_value=10,
            value=1
        )

        milk_type = st.selectbox(
            "Milk Type",
            [
                "Regular",
                "Toned",
                "Almond",
                "Soy",
                "Oat"
            ]
        )

        extras = st.multiselect(
            "Extra Toppings",
            [
                "Honey",
                "Lemon",
                "Chocolate",
                "Cream"
            ]
        )

        special_note = st.text_area(
            "Special Instructions"
        )

        delivery = st.time_input("Delivery Time")

        submit = st.form_submit_button("☕ Make My Tea")

    # ------------------ Output ------------------

    if submit:

        if name == "":
            st.error("Please enter your name.")
            st.stop()

        price = 20 * cups
        price += len(flavors) * 5
        price += len(extras) * 10

        if theme == "Royal":
            price += 20

        if theme == "Healthy":
            price += 10

        st.subheader("Preparing your tea...")

        progress = st.progress(0)

        for i in range(101):
            time.sleep(0.02)
            progress.progress(i)

        st.success("Tea Ready!")

        st.balloons()

        st.markdown("---")

        st.header("📋 Order Summary")

        st.write(f"### 👤 Customer : {name}")
        st.write(f"Age : {age}")

        st.write(f"**Theme:** {theme}")
        st.write(f"**Tea Base:** {tea_base}")
        st.write(f"**Milk Type:** {milk_type}")
        st.write(f"**Strength:** {strength}")
        st.write(f"**Sugar:** {sugar} spoon(s)")
        st.write(f"**Flavors:** {', '.join(flavors) if flavors else 'None'}")
        st.write(f"**Extras:** {', '.join(extras) if extras else 'None'}")
        st.write(f"**Special Note:** {special_note}")
        st.write(f"**Delivery Time:** {delivery}")
        st.write(f"**Cups Ordered:** {cups}")

        st.markdown("---")

        st.metric(
            label="💰 Total Price",
            value=f"₹{price}"
        )

        st.success("Thank you for ordering!")

    # ------------------ Footer ------------------

    st.markdown("---")

    rating = st.slider(
        "⭐ Rate this Chai Maker",
        1,
        5,
        5
    )

    if rating >= 4:
        st.success("Thank you! 😊")

    elif rating == 3:
        st.info("We'll try to improve!")

    else:
        st.warning("Sorry! We'll make better chai next time.")