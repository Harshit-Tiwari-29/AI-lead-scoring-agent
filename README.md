# AI Lead Scoring Agent

An automated, end-to-end **lead identification and prioritization pipeline** designed for business development and go-to-market teams operating in the domains of **toxicology, preclinical safety, and 3D in-vitro research**.

The system identifies relevant professionals, enriches them with research and funding signals, applies a **hybrid rule-based + machine learning scoring framework**, and publishes a ranked, reproducible output through a **public Streamlit dashboard**.

---

## 📊 Live Demo Output

**Public Streamlit Dashboard (Reproducible Output)**  
👉 https://ai-lead-scoring-agent.streamlit.app

The dashboard allows interactive filtering and inspection of ranked leads, making results easy to verify without running the code locally.

---

## 🏛️ High-Level Architecture

The pipeline is orchestrated by `run_pipeline.py`, which wires together four sequential stages executed end-to-end on each run:

**identify → enrich → score → rank & publish**

```python
people = identify_people("data/raw/people_profiles.csv")
enriched = enrich_people(people)
final = rank_and_export(enriched)```

Pipeline Stages
Identification – Filters professionals based on role relevance.

Enrichment – Adds research activity and funding-stage signals.

Scoring – Applies hybrid rule-based and ML-based scoring.

Ranking & Publishing – Produces a ranked CSV and Streamlit dashboard.

🔄 Execution Flow
Stage 1: Identification
Professionals are selected based on role relevance using domain-specific keywords such as toxicology, safety, and preclinical.

```python
Copy code
df["relevant"] = df["job_title"].str.lower().apply(
    lambda x: any(k in x for k in TARGET_KEYWORDS)
)```
Stage 2: Enrichment
Each profile is enriched with:

Publication activity (research intent)

Company funding stage (budget signal)

python
Copy code
df = people_df.merge(publications, on="person_id", how="left")
df = df.merge(funding, on="company", how="left")
To avoid column ambiguity during joins, merged fields are normalized into:

job_title

publication_title

Stage 3: Hybrid Scoring
Two complementary scoring systems are applied:

Rule-based scoring (business intuition)

ML-based scoring (probabilistic intent estimation)

These are blended into a final score.

python
Copy code
final_score = 0.5 * rule_score + 0.5 * ml_score
🧠 Scoring Logic Breakdown
Rule-Based Scoring (Explainable Business Logic)
The rule-based score encodes domain knowledge and commercial relevance.

Signal	Description	Points
Role relevance	Toxicology / safety role	+30
Funding stage	Series A/B/C company	+20
Recent research	Publication in last 2 years	+40
Biotech hub	Boston, Cambridge, Basel, San Diego	+10

Maximum rule-based score: 100

python
Copy code
if row["recent_research"] == 1:
    score += 40
Machine Learning Scoring (Probability Estimation)
A Logistic Regression model estimates the likelihood that a lead is high-intent based on engineered features:

Seniority (senior_role)

Funding signal (funded_company)

Research activity (recent_research)

Location hub (hub_location)

python
Copy code
model.predict_proba(X)[:, 1]
The probability output is scaled to a 0–100 score.

Hybrid Final Score
To balance explainability and robustness, the final score blends both approaches:

python
Copy code
final_score = 0.5 * rule_score + 0.5 * ml_score
This mirrors real-world lead-scoring systems used in CRM and sales intelligence platforms.

🧠 Key Design Decisions & Problems Solved
1. Explainability Over Black-Box ML
Pure ML models lack transparency for business teams. A hybrid approach ensures interpretability while benefiting from probabilistic ranking.

2. Column Collision During Dataset Joins
Ambiguous columns (title_x, title_y) were resolved early by canonical renaming, preventing downstream pipeline and UI failures.

3. Ethical & Legal Data Usage
No LinkedIn scraping or private data is used. All datasets follow publicly observable research and industry patterns.

4. Meaningful Validation Dataset
The dataset contains 50+ realistic leads with variation across seniority, geography, funding stage, and research activity—sufficient to demonstrate real ranking behavior.

5. UI Stability & Backward Compatibility
The Streamlit UI dynamically adapts to available scoring columns, preventing runtime errors when scoring logic evolves.

🛠️ Tech Stack
Python 3.x

Pandas – data processing

Scikit-learn – logistic regression model

Streamlit – interactive dashboard

GitHub – version control and reproducibility

📁 Project Structure
powershell
Copy code
ai-lead-scoring-agent/
│
├── src/
│   ├── identification.py   # Lead identification logic
│   ├── enrichment.py       # Research & funding enrichment
│   ├── scoring.py          # Rule-based scoring
│   ├── ml_features.py      # ML feature engineering
│   ├── ml_model.py         # Logistic regression model
│   └── ranking.py          # Hybrid scoring & ranking
│
├── data/
│   ├── raw/                # Input datasets
│   └── processed/          # Ranked output
│
├── app.py                  # Streamlit frontend
├── run_pipeline.py         # End-to-end pipeline runner
├── requirements.txt
└── README.md
🔧 Local Setup
Clone and create a virtual environment:

bash
Copy code
git clone <repo-url>
cd ai-lead-scoring-agent
python -m venv .venv
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the pipeline:

bash
Copy code
python run_pipeline.py
Launch the dashboard:

bash
Copy code
streamlit run app.py
📡 Reproducibility & Compliance
No private or scraped data

No LinkedIn scraping

Deterministic, inspectable pipeline

Fully reproducible outputs

Designed for easy verification by assignment reviewers

☁️ Deployment
The application is deployed publicly using Streamlit Community Cloud, allowing reviewers to verify results without local setup.

🎯 Design Philosophy
Business-first scoring logic

Explainable machine learning

Modular, production-style structure

Focus on ranking quality and clarity
