# quiz-app-dashboard
# 🧠 Streamlit Quiz App

An interactive quiz application built using **Python** and **Streamlit**, supporting multiple subjects, difficulty levels, and a modern background UI.

---

## 🚀 Features

- 🎯 Topic- and difficulty-based question selection
- 🧾 Multiple-choice questions from `question.json`
- 🖼️ Custom background image
- 📈 Real-time progress bar
- ✅ Instant feedback after submission

---

## 📂 Project Structure
quiz_app_streamlit/
├── app.py # Main Streamlit app
├── questions.json # Quiz data file (edit/add questions here)
├── background.jpg # Background image for UI
├── README.md # Project documentation
├── requirements.txt # Dependencies


---

## 🖥️ Screenshots


---![Screenshot (29)](https://github.com/user-attachments/assets/69e77f1a-9226-4229-9d8d-0caef6fc4916)

![Screenshot (29)](https://github.com/user-attachments/assets/44683cc9-2b30-4c25-b087-d5a8fd90030e)

## ⚙️ Installation & Run

### 🔧 Prerequisites

- Python 3.8 or above
- pip installed

### 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/y2023s/quiz_app_streamlit.git
cd quiz_app_streamlit

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

📄 Format of questions.json
[
  {
    "topic": "Math",
    "difficulty": "easy",
    "question": "What is 2 + 2?",
    "options": ["2", "3", "4", "5"],
    "answer": "4"
  }
}


