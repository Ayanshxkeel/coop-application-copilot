# Co-op Application Copilot

A local job application tracker with a simple skill comparison. Paste a posting and resume text; the app looks for terms in a small editable Python skill list. It does **not** infer ability or write resume claims for you.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Try it

Paste `I used Python and SQL in a class project` into the resume box. Save a job with a company and role using the example posting. Select it. Python and SQL should appear under matches; Excel and Power BI should appear as review gaps. Change its status to Applied and refresh; it should remain Applied.

Data is stored in a local `applications.db` SQLite file. To start fresh, stop the app and delete that file. The skill vocabulary is in `logic.py`; you can extend it. This is keyword matching, not a recruiter score or a live job feed.
