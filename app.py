import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


from modules.resume_parser import (
    extract_text,
    extract_email,
    extract_phone,
    extract_name
)
from modules.analyzer import analyze_resume
from modules.interview import generate_questions, check_answer
from database.database import create_database, save_data, get_all_data

create_database()


st.title(
"🤖 AI Resume Analyzer & Interview Coach"
)

st.sidebar.title(
"Dashboard"
)


st.sidebar.write(
"""
### Features

✔ Resume Analysis

✔ Skill Detection

✔ Resume Score

✔ AI Interview Questions

✔ Answer Feedback
    
✔ Result Storage
"""
)

st.write(
"Improve your resume and prepare for interviews using AI"
)

name = st.text_input(
"Enter your name"
)

st.write(
"Upload Resume and get AI feedback"
)

st.subheader(
"📄 Upload Resume"
)


resume = st.file_uploader(
"Choose your PDF Resume",
type=["pdf"]
)

if resume:


    st.success(
    "Resume Uploaded Successfully"
    )


    resume_text = extract_text(resume)
    name_from_resume = extract_name(resume_text)

    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    st.subheader("👤 Candidate Information")

    st.write("**Name:**", name_from_resume)

    st.write("**Email:**", email)

    st.write("**Phone:**", phone)



    st.subheader(
    "Resume Analysis"
    )



    skills, missing, score = analyze_resume(
        resume_text
    )



    st.write(
    "Skills Found:"
    )


    for skill in skills:

     st.success(
     skill
    )



    st.write(
    "Resume Score:"
    )


    st.progress(
    score/100
    )


    st.metric(
    label="Resume Score",
    value=str(score)+"/100"
)


    st.write(
    "Suggested Skills To Add:"
    )


    st.write(
    missing
    )

    st.subheader(
    "🎤 AI Generated Interview Questions"
    )


    questions = generate_questions(
        skills
    )


    for q in questions:


        st.write(
        "• " + q
        )

        st.subheader(
    "Practice Interview"
    )


    user_answer = st.text_area(
    "Write your answer here"
    )


if st.button(
    "Check Answer"
):


    ans_score, feedback = check_answer(
        user_answer
    )


    st.session_state["ans_score"] = ans_score


    st.write(
    "Answer Score:"
    )


    st.progress(
    ans_score/100
    )


    st.write(
    str(ans_score)+"/100"
    )


    st.success(
    feedback
    )
if st.button(
    "Save Result"
):


    interview_score = st.session_state.get(
        "ans_score",
        0
    )


    save_data(
    name,
    str(skills),
    score,
    interview_score
    )


    st.success(
    "Data Saved Successfully"
    )

    st.markdown(
"""
---
Created using Python | Streamlit | AI
"""
)
    
st.subheader("📊 Admin Dashboard")

if st.button("View All Candidates"):

    data = get_all_data()

    if data:

        for row in data:

            st.write(f"ID: {row[0]}")
            st.write(f"Name: {row[1]}")
            st.write(f"Skills: {row[2]}")
            st.write(f"Resume Score: {row[3]}")
            st.write(f"Interview Score: {row[4]}")
            st.write("--------------------------")

    else:
        st.warning("No records found.")