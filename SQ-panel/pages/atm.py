

import streamlit as st

# Initialize user balance and password
my_balance = 10000
my_password = "ab1234"

# Set Page Title
st.title("🏧 ATM Machine")

# Password Input
password = st.text_input("Enter your Password", type="password")

if password:
    if password == my_password:
        st.success("✅ Your password is correct. Login successful!")

        # Select Operation
        operation = st.radio("Select one option", ["Cash Withdraw", "Check Balance"])

        if operation == "Cash Withdraw":
            amount = st.number_input("Enter Amount to Withdraw", min_value=1, step=1)

            if st.button("Withdraw"):
                if amount > my_balance:
                    st.error("❌ You have insufficient balance.")
                else:
                    my_balance -= amount
                    st.success(f"💸 {amount} successfully withdrawn!")
                    st.info(f"💰 Your Remaining Balance: {my_balance}")

        elif operation == "Check Balance":
            st.info(f"💰 Your Account Balance: {my_balance}")

    else:
        st.error("❌ Your Password is incorrect. Try Again!")
