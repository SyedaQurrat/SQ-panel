
import streamlit as st
import random

# Set Page Title
st.title("🎯 Dynamic Quiz Game")

# Questions Bank
quiz_data = {
    "TypeScript": [
        {"question": "What is TypeScript?", "options": ["A JS library", "A JS framework", "A superset of JavaScript", "A programming language"], "answer": "A superset of JavaScript"},
        {"question": "Which keyword defines a variable in TypeScript?", "options": ["var", "let", "const", "All of the above"], "answer": "All of the above"},
        {"question": "How do you define an array in TypeScript?", "options": ["let arr: number[]", "let arr = number()", "let arr: []", "let arr = {}"], "answer": "let arr: number[]"},
        {"question": "How to enforce strict type checking in TypeScript?", "options": ["Using tsconfig.json", "Using strictMode", "Using `strict` keyword", "It is always enforced"], "answer": "Using tsconfig.json"},
        {"question": "Which command compiles TypeScript to JavaScript?", "options": ["tsc filename.ts", "compile filename.ts", "transpile filename.ts", "run filename.ts"], "answer": "tsc filename.ts"}
    ],
    "Python": [
        {"question": "What is the correct file extension for Python files?", "options": [".python", ".py", ".pyt", ".pt"], "answer": ".py"},
        {"question": "Which keyword creates a function in Python?", "options": ["function", "def", "fun", "define"], "answer": "def"},
        {"question": "Which operator is used for exponentiation?", "options": ["^", "**", "//", "*"], "answer": "**"},
        {"question": "What is the output of print(2 * 3 ** 2)?", "options": ["18", "36", "12", "16"], "answer": "18"},
        {"question": "Which data type is mutable?", "options": ["tuple", "string", "list", "int"], "answer": "list"}
    ],
    "HTML": [
        {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "Hyper Transfer Markup Language", "Hyper Transfer Mark Language", "HyperText Mark Language"], "answer": "HyperText Markup Language"},
        {"question": "Which HTML tag is for the largest heading?", "options": ["<heading>", "<h6>", "<h1>", "<head>"], "answer": "<h1>"},
        {"question": "Which attribute is for a unique element?", "options": ["class", "id", "name", "style"], "answer": "id"},
        {"question": "Which tag is for a hyperlink?", "options": ["<a>", "<link>", "<href>", "<url>"], "answer": "<a>"},
        {"question": "What is the default display of a `<div>`?", "options": ["inline", "inline-block", "block", "flex"], "answer": "block"}
    ],
    "CSS":[
        {"question": "What does CSS stand for?", "options": ["Cascading Style Sheets ", "Cascading Style Script", "Cascading Style Code", "Cascading Style Language"], "answer": "Cascading Style Sheets "},
        {"question": "Which CSS property is used to set the background color?", "options": [" background-color", "color", "text-color", "bg-color"], "answer": "background-color "},
        {"question": "Which CSS property is used to set the font size?", "options": [" font-size", "size", "text-size", "fs"], "answer": "font-size"},
        {"question": "Which CSS property is used to set the text color?", "options": [" color", "text-color", "text", "tc"], "answer": "color"},
        {"question": "Which CSS property is used to set the text alignment?", "options": [" text-align", "align", "align-text", "ta"], "answer": "text-align"},
    ],
    "JavaScript": [
        {"question": "What is JavaScript?", "options": ["A programming language", "A library ", "A framework", "A language for web development"], "answer": "A programming language"},
        {"question": "Which keyword is used to declare a variable in JavaScript?", "options": [" var", "let", "const", "All of the above"], "answer": "All of the above"},
        {"question": "How do you get the value of an HTML element in JavaScript?", "options ": ["document.getElementById()", "document.getelementById()", "document.getElementById", "document.getelementById "], "answer": "document.getElementById()"},
        {"question": "How do you create a function in JavaScript?", "options": ["function", "def", "fun", "define"], "answer": "function"},
        {"question": " What is JavaScript?", "options": ["A programming language", "A library ", "A framework", "A language for web development"], "answer": "A programming language"},
        ],

    
}

# Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.selected_category = None
    st.session_state.questions = []
    st.session_state.selected_option = None
    st.session_state.user_answers = []  # Fix: Store user answers

# User Name Input
if not st.session_state.quiz_started:
    user_name = st.text_input("Please enter your name:")
    
    if user_name:
        categories = list(quiz_data.keys())  
        category = st.selectbox("Choose a quiz category:", categories)
        
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.selected_category = category
            st.session_state.questions = random.sample(quiz_data[category], 5)
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.selected_option = None
            st.session_state.user_answers = []  # Reset user answers
            st.rerun()

# Show Questions One by One
if st.session_state.quiz_started:
    question_index = st.session_state.current_question
    if question_index < len(st.session_state.questions):
        question = st.session_state.questions[question_index]
        st.subheader(f"Q{question_index + 1}: {question['question']}")
        
        # No Pre-selected Answer
        selected_option = st.radio("Choose your answer:", question["options"], key=f"q{question_index}", index=None)
        
        if st.button("Next Question"):
            if selected_option:  # Check if user selected an option
                # Store User Answer
                st.session_state.user_answers.append({"question": question["question"], "selected": selected_option, "correct": question["answer"]})
                
                if selected_option == question["answer"]:
                    st.session_state.score += 10
                    
                st.session_state.current_question += 1
                st.session_state.selected_option = None
                st.rerun()
            else:
                st.warning("⚠️ Please select an answer before proceeding!")

    else:
        st.subheader(f"🎉 Your total score: {st.session_state.score}/50")
        
        st.write("### 📜 **Review Your Answers:**")
        for idx, ans in enumerate(st.session_state.user_answers):
            st.write(f"**Q{idx + 1}: {ans['question']}**")
            st.write(f"👉 Your Answer: `{ans['selected']}`")
            st.write(f"✅ Correct Answer: `{ans['correct']}`")
            if ans['selected'] == ans['correct']:
                st.success("🎯 Correct!")
            else:
                st.error("❌ Wrong Answer!")
            st.write("---")

        if st.button("🔄 Play Again"):
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.selected_category = None
            st.session_state.questions = []
            st.session_state.selected_option = None
            st.session_state.user_answers = []  # Reset answers
            st.rerun()


