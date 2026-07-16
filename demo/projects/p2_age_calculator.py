from datetime import date
from dateutil.relativedelta import relativedelta
import streamlit as st


def age_calculator():
    st.title("🎂 Age Calculator")

    today = date.today()

    birth_date = st.date_input(
        "Select your birth date",
        value=date(2007, 7, 25),
        min_value=date(1950, 1, 1),
        max_value=today,
    )

    option = st.radio(
        "Reference Date",
        ["Current Date", "Custom Date"],
        horizontal=True,
    )

    if option == "Current Date":
        current_date = today
    else:
        current_date = st.date_input(
            "Select reference date",
            value=today,
            min_value=birth_date,
            max_value=today,
        )

    if st.button("Calculate Age"):

        if current_date < birth_date:
            st.error("Reference date cannot be before birth date.")
            return

        age = relativedelta(current_date, birth_date)
        total_days = (current_date - birth_date).days

        view = st.selectbox(
            "Show Age In",
            ["Years, Months & Days", "Years", "Months", "Days"],
        )

        if view == "Years, Months & Days":
            st.success(
                f"🎉 You are **{age.years} years, {age.months} months, and {age.days} days** old."
            )

        elif view == "Years":
            st.success(f"🎉 You are **{age.years} years** old.")

        elif view == "Months":
            total_months = age.years * 12 + age.months
            st.success(f"🎉 You are **{total_months} months** old.")

        else:
            st.success(f"🎉 You are **{total_days:,} days** old.")
