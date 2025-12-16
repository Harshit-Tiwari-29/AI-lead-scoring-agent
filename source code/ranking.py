from src.scoring import calculate_score
from src.ml_features import create_ml_features
from src.ml_model import train_ml_model

ML_FEATURES = [
    "senior_role",
    "funded_company",
    "recent_research",
    "hub_location"
]

def rank_and_export(df):
    # ---------------- Rule-based score ----------------
    df["rule_score"] = df.apply(calculate_score, axis=1)

    # ---------------- ML features ----------------
    df = create_ml_features(df)

    # ---------------- Train ML model ----------------
    model = train_ml_model(df)

    # ---------------- ML prediction ----------------
    df["ml_probability"] = model.predict_proba(df[ML_FEATURES])[:, 1]
    df["ml_score"] = (df["ml_probability"] * 100).round(2)

    # ---------------- Final blended score ----------------
    df["final_score"] = (
        0.5 * df["rule_score"] + 0.5 * df["ml_score"]
    ).round(2)

    # ---------------- Ranking ----------------
    df = df.sort_values("final_score", ascending=False)
    df["rank"] = range(1, len(df) + 1)

    # ---------------- Export ----------------
    df.to_csv("data/processed/final_ranked_leads.csv", index=False)

    return df
