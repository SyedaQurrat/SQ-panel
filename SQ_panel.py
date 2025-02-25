





import streamlit as st

# # Set Page Title & Layout
st.set_page_config(page_title="SQ Panel", layout="wide")

# Sidebar
with st.sidebar:

    st.title("SQ Panel")  # Sidebar Title

    # Add Logo & Description
    st.markdown(
        """
        <p style="text-align: center; font-size: 14px;">
        Welcome to SQ Panel! This dashboard allows you to navigate through multiple projects.
        Select any project from the list to get started.
        </p>
        """, unsafe_allow_html=True
    )

    # Define Projects List
    projects = {
        "Calculator": "pages/calculator.py",
        "To-Do List": "pages/todo.py",
        "Word Counter": "pages/word_counter.py",
        "BMI Calculator": "pages/bmi.py",
        "ATM Machine": "pages/atm.py",
        "Quiz": "pages/quiz.py"
        
    }

    # Sidebar Navigation
    selected_project = st.radio("Select a Project:", list(projects.keys()))

    # 👇 Created by text at the bottom
    st.markdown("---")  # Horizontal Line
    st.markdown("<p style='text-align: center;'>Created by <b>Syeda Qurrat</b></p>", unsafe_allow_html=True)

# Right Section (Loading Selected Project)
st.header(f"📌 {selected_project}")  # Show Selected Project Name

if selected_project:
    exec(open(projects[selected_project], encoding="utf-8").read())  # Run Selected Project
