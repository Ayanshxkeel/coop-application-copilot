import re
import sqlite3
from pathlib import Path

SKILLS = ["python", "sql", "excel", "power bi", "pandas", "data analysis", "machine learning", "statistics", "git", "apis", "flask", "react", "communication", "testing", "automation"]


def found_skills(text):
    words = " " + re.sub(r"[^a-z0-9+#]+", " ", text.lower()) + " "
    return [skill for skill in SKILLS if " " + skill + " " in words]


def compare(resume, posting):
    required = set(found_skills(posting))
    evidence = set(found_skills(resume))
    return sorted(required & evidence), sorted(required - evidence)


def connect(path="applications.db"):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE IF NOT EXISTS applications (id INTEGER PRIMARY KEY, company TEXT NOT NULL, role TEXT NOT NULL, deadline TEXT, status TEXT NOT NULL, posting TEXT NOT NULL)")
    db.commit()
    return db


def add_application(db, company, role, deadline, status, posting):
    if not company.strip() or not role.strip() or not posting.strip():
        raise ValueError("Company, role, and posting are required.")
    db.execute("INSERT INTO applications(company,role,deadline,status,posting) VALUES (?,?,?,?,?)", (company.strip(), role.strip(), deadline, status, posting.strip()))
    db.commit()


def all_applications(db):
    return db.execute("SELECT id,company,role,deadline,status,posting FROM applications ORDER BY id DESC").fetchall()


def update_status(db, app_id, status):
    db.execute("UPDATE applications SET status=? WHERE id=?", (status, app_id))
    db.commit()
