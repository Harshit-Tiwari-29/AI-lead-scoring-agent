from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

FEATURES = [
    "senior_role",
    "funded_company",
    "recent_research",
    "hub_location"
]

def train_ml_model(df):
    X = df[FEATURES]
    y = (df["rule_score"] >= 70).astype(int)

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression())
    ])

    model.fit(X, y)
    return model
