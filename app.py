import streamlit as st
import json
import base64

def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("bg.png")  # 👈 Add this line near the top


# Page settings
st.set_page_config(page_title="Filtered Quiz App", layout="centered")
st.title("🧠 Quiz App with Filters")

# Load JSON questions
json_path = "C:\\Users\\2023s\\Desktop\\quiz_app_streamlit\\question.json"

try:
    with open(json_path, "r", encoding="utf-8") as f:
        all_questions = json.load(f)
except Exception as e:
    st.error(f"Error loading questions: {e}")
    st.stop()

# Get unique topics and difficulty levels
topics = sorted(set(q.get("topic", "Unknown") for q in all_questions if "topic" in q))
difficulties = sorted(set(q.get("difficulty", "Unknown") for q in all_questions if "difficulty" in q))


# Session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "filtered_questions" not in st.session_state:
    st.session_state.filtered_questions = []

# Filter form
with st.sidebar:
    st.header("🧾 Filter Settings")
    selected_topic = st.selectbox("Choose Topic", topics)
    selected_difficulty = st.selectbox("Choose Difficulty", difficulties)

    if st.button("Start Quiz"):
        # Filter questions
        st.session_state.filtered_questions = [
            q for q in all_questions if q["topic"] == selected_topic and q["difficulty"] == selected_difficulty
        ]
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.rerun()

questions = st.session_state.filtered_questions
q_index = st.session_state.q_index
total_questions = len(questions)

# If questions selected
if total_questions > 0 and q_index < total_questions:
    q = questions[q_index]

    st.markdown(f"### Question {q_index + 1} of {total_questions}")
    st.progress(min((q_index + 1) / total_questions, 1.0))
    st.info(f"🎯 Score: {st.session_state.score}")
    
    st.subheader(f"📚 {q['question']}")
    selected = st.radio("Your answer:", q['options'], key=q_index)

    if st.button("Submit Answer"):
        if selected == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! Correct answer: {q['answer']}")
        st.session_state.q_index += 1
        st.rerun()

# Quiz complete
elif total_questions > 0 and q_index >= total_questions:
    st.success("🎉 Quiz Complete!")
    st.markdown(f"### ✅ Final Score: `{st.session_state.score} / {total_questions}`")
    if st.button("🔁 Restart"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.filtered_questions = []
        st.rerun()
else:
    st.warning("📌 Use the sidebar to choose topic & difficulty to start the quiz.")
