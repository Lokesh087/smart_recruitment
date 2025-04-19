import streamlit as st
import sqlite3
import pandas as pd
import PyPDF2, docx2txt, re
from email.message import EmailMessage
import smtplib

# --- CONFIG ---
RECRUITER_EMAIL = "recruitersmail@gmail.com"  # <-- CHANGE THIS
SENDER_EMAIL = "senders5@gmail.com"
SENDER_PASSWORD = "senders.passwords"

# --- DB SETUP ---
conn = sqlite3.connect('candidates.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    degree TEXT,
    resume_score INTEGER,
    aptitude_score INTEGER,
    coding_score INTEGER,
    total_score INTEGER,
    category TEXT,
    resume_text TEXT
)''')
conn.commit()

# --- UTILS ---
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return ''.join([p.extract_text() for p in reader.pages])
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        return docx2txt.process(file)
    return ""

def extract_degree(text):
    degrees = ["PhD", "Doctorate", "Masters", "Master", "Bachelor", "B.Tech", "B.E", "Diploma"]
    for d in degrees:
        if re.search(d, text, re.IGNORECASE):
            return d
    return "Unknown"

def calculate_resume_score(text):
    keywords = {
        "machine learning": 10, "deep learning": 10,
        "python": 5, "certified": 5,
        "publications": 10, "hackathon": 5,
        "data science": 10, "nlp": 5
    }
    return sum(points for k, points in keywords.items() if k in text.lower())

def categorize(degree, r, a, c):
    total = r + a + c
    if degree.lower() == "phd" or total > 60:
        return "Top Tier"
    elif degree.lower() in ["masters", "master", "bachelor", "b.tech", "b.e"] and total >= 40:
        return "Mid Tier"
    else:
        return "Entry Level"

def send_email(candidate_data):
    msg = EmailMessage()
    msg['Subject'] = f"New Candidate: {candidate_data['name']} ({candidate_data['category']})"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECRUITER_EMAIL
    content = f"""
📄 Name: {candidate_data['name']}
📧 Email: {candidate_data['email']}
🎓 Degree: {candidate_data['degree']}
📊 Total Score: {candidate_data['total_score']}/110
🏆 Category: {candidate_data['category']}
"""
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email sending failed: {e}")
        return False

# --- STREAMLIT APP ---
st.set_page_config(page_title="Smart Recruiter", layout="centered")
st.title("🤖 Smart Recruitment Chatbot")

menu = st.sidebar.radio("Menu", ["Submit Resume", "Admin Dashboard"])

if menu == "Submit Resume":
    with st.form("candidate_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
        aptitude = st.slider("Aptitude Test Score (0–30)", 0, 30, 15)
        coding = st.slider("Coding Test Score (0–30)", 0, 30, 20)
        submit = st.form_submit_button("Evaluate")

    if submit and file:
        text = extract_text(file)
        degree = extract_degree(text)
        resume_score = calculate_resume_score(text)
        total = resume_score + aptitude + coding
        category = categorize(degree, resume_score, aptitude, coding)

        # Save to DB
        c.execute('''INSERT INTO candidates 
            (name, email, degree, resume_score, aptitude_score, coding_score, total_score, category, resume_text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (name, email, degree, resume_score, aptitude, coding, total, category, text))
        conn.commit()

        # Email Recruiter
        email_data = {
            "name": name,
            "email": email,
            "degree": degree,
            "total_score": total,
            "category": category
        }
        sent = send_email(email_data)

        st.success(f"🎯 You’ve been classified as a **{category}** candidate!")
        if sent:
            st.info("📩 Recruiter notified by email.")

elif menu == "Admin Dashboard":
    st.subheader("📊 All Submitted Candidates")
    df = pd.read_sql_query("SELECT name, email, degree, resume_score, aptitude_score, coding_score, total_score, category FROM candidates", conn)
    st.dataframe(df)
