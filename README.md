# Co-op Application Copilot

Keep job applications in one local tracker and compare the skills mentioned in a posting with terms in a resume you paste.

## Features

- Saves company, role, deadline, posting, and application status.
- Shows which terms from a small editable skill list occur in a selected posting and pasted resume.
- Counts skills across saved postings so you can see recurring requirements.
- Stores application records locally in SQLite.

## Run locally

```bash
git clone https://github.com/Ayanshxkeel/coop-application-copilot.git
cd coop-application-copilot
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit. On Windows, activate with `.venv\Scripts\activate`.

## Try it

Paste `I used Python and SQL in a class project` into the resume box. Save a company and role with the included example posting. Select it: Python and SQL should be matches, while Excel and Power BI should appear as terms to review. Change the status to **Applied** and refresh to confirm it persists.

## How it works

`logic.py` creates the SQLite table and saves or updates applications. `found_skills()` searches for terms from the `SKILLS` list; `compare()` intersects the posting terms with the pasted resume terms. `app.py` displays the forms, status control, and skill counts.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Application tracker interface |
| `logic.py` | Storage and keyword comparison |
| `requirements.txt` | Python dependencies |

## Data and limitations

Application records are stored in local `applications.db`. The pasted resume is used during the current app session; it is not saved by the app. Stop the app and delete the database to reset. This is **keyword matching**, not a recruiter score or a live job feed. A missing term is not proof you lack a skill; only add truthful experience to a resume.
