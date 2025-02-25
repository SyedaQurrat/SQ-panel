
import streamlit as st

# Page Title
st.markdown("<h1 style='text-align: center; color: white;'>Simple Calculator with History</h1>", unsafe_allow_html=True)

# Initialize session state for expression and history
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "history" not in st.session_state:
    st.session_state.history = []

# Function to update expression
def update_expression(value):
    st.session_state.expression += str(value)
    st.rerun()

# Function to evaluate expression
def calculate_result():
    try:
        result = eval(st.session_state.expression, {'__builtins__': None}, {})

        # Convert float to int if no decimal part
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        # Save calculation to history
        st.session_state.history.append(f"{st.session_state.expression} = {result}")
        
        # Store result as new expression
        st.session_state.expression = str(result)

    except:
        st.session_state.expression = "Error"

    st.rerun()

# Function to clear expression
def clear_expression():
    st.session_state.expression = ""
    st.rerun()

# Function to clear history
def clear_history():
    st.session_state.history = []
    st.rerun()

# Custom Styling for Better UI
st.markdown(
    """
    <style>
        div[data-testid="stTextInput"] input {
            text-align: right;
            font-size: 30px;
            font-weight: bold;
        }
        div[data-testid="stButton"] button {
            width: 100%;
            height: 60px;
            font-size: 24px;
            font-weight: bold;
        }
        .history-container {
            background-color: #222;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display input field with real-time expression
st.text_input("Calculation:", value=st.session_state.expression, key="calc_display", disabled=True)

# Button Layout in a Grid
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "×"],  # "×" symbol used instead of "*"
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons using columns for better UI
for row in buttons:
    cols = st.columns(4, gap="small")  # Adjust spacing for better layout
    for i, button in enumerate(row):
        if cols[i].button(f"**{button}**", key=button):  # **Bold** button text
            if button == "=":
                calculate_result()
            elif button == "C":
                clear_expression()
            elif button == "×":  # Replace "×" with "*" when storing expression
                update_expression("*")
            else:
                update_expression(button)

# Show calculation history
st.markdown("### Calculation History 📝")

# Show history in a box
with st.container():
    for entry in st.session_state.history[::-1]:  # Reverse to show latest first
        st.markdown(f"<p style='font-size:18px; color:white;'>{entry}</p>", unsafe_allow_html=True)

# Clear history button
if st.button("Clear History"):
    clear_history()
