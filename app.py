import pandas as pd
import streamlit as st
from logic import add_application, all_applications, compare, connect, found_skills, update_status

st.set_page_config(page_title="Co-op Application Copilot", page_icon="🧭", layout="wide")
st.title("Co-op Application Copilot")
st.caption("Track real applications and find skills that appear across the jobs you want.")
db = connect()
sample = "We seek a program analyst with Python, SQL, Excel, Power BI, data analysis, communication, and testing experience."
resume = st.text_area("Paste your resume text", height=160, placeholder="Paste your own resume here. Nothing is sent to an AI service.")
with st.form("new_job"):
    a, b, c = st.columns(3)
    company = a.text_input("Company")
    role = b.text_input("Role")
    deadline = c.date_input("Deadline", value=None)
    posting = st.text_area("Job posting", value=sample, height=120)
    if st.form_submit_button("Save application"):
        try:
            add_application(db, company, role, str(deadline or ""), "Saved", posting)
            st.success("Application saved.")
        except ValueError as error:
            st.error(str(error))

rows = all_applications(db)
if rows:
    st.subheader("Your applications")
    table = pd.DataFrame(rows, columns=["ID", "Company", "Role", "Deadline", "Status", "Posting"])
    st.dataframe(table.drop(columns="Posting"), hide_index=True, width="stretch")
    selected = st.selectbox("Inspect a posting", rows, format_func=lambda row: f"{row[1]} — {row[2]}")
    matched, missing = compare(resume, selected[5]) if resume.strip() else ([], found_skills(selected[5]))
    col1, col2 = st.columns(2)
    col1.metric("Skills mentioned in posting", len(found_skills(selected[5])))
    col2.metric("Found in pasted resume", len(matched))
    st.write("**Found in your resume:**", ", ".join(matched) or "None yet")
    st.write("**Review these gaps:**", ", ".join(missing) or "None from the built-in skill list")
    st.info("A missing keyword is a prompt to review your experience, not proof that you lack the skill. Only add truthful evidence to your resume.")
    with st.expander("Original posting"):
        st.write(selected[5])
    new_status = st.selectbox("Update status", ["Saved", "Applied", "Interview", "Offer", "Closed"], index=["Saved", "Applied", "Interview", "Offer", "Closed"].index(selected[4]))
    if st.button("Save status"):
        update_status(db, selected[0], new_status)
        st.rerun()
    counts = pd.Series([skill for row in rows for skill in found_skills(row[5])]).value_counts()
    st.subheader("Skills across saved postings")
    st.bar_chart(counts)
else:
    st.info("Add your first real posting to start. Your data is saved locally in applications.db.")
