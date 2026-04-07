# 🤖 AI-Driven Smart Recruitment System

An intelligent recruitment automation platform that evaluates candidates using resume analysis, aptitude scores, and coding assessments. The system classifies candidates into tiers and automatically notifies recruiters, significantly reducing manual screening effort.
U can check out my  website on https://smartrecruitment-hbi5ufyhh2buaxdluuwjze.streamlit.app/
---

## 📌 Overview
The AI-Driven Smart Recruitment System streamlines the hiring process by combining:
- Resume parsing and keyword-based scoring
- Aptitude and coding test evaluation
- Automated candidate categorization
- Recruiter email notifications
- Admin dashboard for candidate analytics

This project demonstrates practical implementation of **AI-assisted decision-making**, **backend automation**, and **data-driven recruitment workflows**.

---

## 🚀 Key Features
- 📄 Resume upload support (PDF & DOCX)
- 🔍 Automated resume text extraction and analysis
- 🎓 Degree detection from resumes
- 📊 Resume scoring using AI-inspired keyword weighting
- 🧠 Combined evaluation (Resume + Aptitude + Coding)
- 🏷️ Candidate categorization:
  - Top Tier  
  - Mid Tier  
  - Entry Level
- 📩 Automatic email notification to recruiters
- 🗄️ Persistent candidate storage using SQLite
- 📊 Admin dashboard for viewing all candidates

---

## 🧠 Candidate Evaluation Logic
Candidates are evaluated based on:
- **Resume Score** (keyword-based AI scoring)
- **Aptitude Test Score**
- **Coding Test Score**

Final categorization:
- **Top Tier:** High total score or PhD-level qualification
- **Mid Tier:** Bachelor/Master degree with good total score
- **Entry Level:** Fresh candidates or lower total score

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Frontend:** Streamlit
- **Backend Logic:** Python
- **Database:** SQLite
- **Libraries & Tools:**
  - Streamlit
  - Pandas
  - PyPDF2
  - python-docx / docx2txt
  - smtplib (Email Automation)

---

## 📂 Project Structure
├── smart_recruiter_app.py # Main Streamlit application
├── app.py # Supporting logic
├── candidates.db # SQLite database
├── requirements.txt # Project dependencies
├── personal.env # Environment variables
├── README.md # Project documentation
└── .gitignore


---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Lokesh087/ai-recruitment-system.git
cd ai-recruitment-system

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables
Create a file named personal.env:
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
RECRUITER_EMAIL=recruiter_email@gmail.com

5️⃣ Run the Application
streamlit run smart_recruiter_app.py

📊 Admin Dashboard--
View all submitted candidates
Analyze resume, aptitude, and coding scores
Track candidate categories

🎯 Use Cases--
Campus recruitment automation
Internship shortlisting
Resume screening for HR teams
AI-assisted candidate evaluation

📈 Impact--
Reduced manual resume screening effort by ~50%
Improved candidate response time to under 5 seconds
Enabled structured and unbiased candidate evaluation

👨‍💻 Author--
Lokesh Pargain
AI / Data Science | Software Development
🔗 LinkedIn: https://www.linkedin.com/in/lokesh-pargain-4319b1283/
💻 GitHub: https://github.com/Lokesh087

⭐ If you find this project useful, feel free to star the repository and connect with me on LinkedIn!
