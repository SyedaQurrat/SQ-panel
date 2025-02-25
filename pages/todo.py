
import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "editing_task" not in st.session_state:
    st.session_state.editing_task = None  # Track which task is being edited
if "task_input" not in st.session_state:
    st.session_state.task_input = ""  # Ensure input field resets properly

# App Title
st.title("📝 To-Do List App")

# Input field for new task
new_task = st.text_input("Add a new task:", value=st.session_state.task_input, key="task_input")

# Add task function
def add_task():
    if st.session_state.task_input.strip():
        st.session_state.tasks.append({"task": st.session_state.task_input, "completed": False})
        st.session_state.task_input = ""  # ✅ Clear input without st.rerun()

# Add Task button
st.button("➕ Add Task", on_click=add_task)

# Display tasks
st.subheader("Your Tasks:")
for index, task in enumerate(st.session_state.tasks):
    col1, col2, col3, col4 = st.columns([0.1, 0.6, 0.1, 0.1])

    # Checkbox for completed task
    with col1:
        checked = st.checkbox("", value=task["completed"], key=f"chk_{index}")
        if checked != task["completed"]:
            st.session_state.tasks[index]["completed"] = checked

    # Task text (Strike-through if completed)
    with col2:
        if index == st.session_state.editing_task:
            edited_task = st.text_input("Edit Task:", value=task["task"], key=f"edit_input_{index}")
            if st.button("💾 Save", key=f"save_{index}"):
                st.session_state.tasks[index]["task"] = edited_task
                st.session_state.editing_task = None
        else:
            st.write(f"~~{task['task']}~~" if task["completed"] else task["task"])

    # Edit button
    with col3:
        if st.button("✏️", key=f"edit_{index}"):
            st.session_state.editing_task = index

    # Delete button
    with col4:
        if st.button("❌", key=f"del_{index}"):
            del st.session_state.tasks[index]
            st.session_state.editing_task = None

# Clear All button
if st.button("🗑 Clear All"):
    st.session_state.tasks = []
    st.session_state.editing_task = None
