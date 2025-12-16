import pandas as pd

TARGET_KEYWORDS = [
    "toxicology", "safety", "preclinical", "hepatic", "3d"
]

def identify_people(path):
    df = pd.read_csv(path)
    df["title_clean"] = df["title"].str.lower()

    df["relevant"] = df["title_clean"].apply(
        lambda x: any(k in x for k in TARGET_KEYWORDS)
    )

    return df[df["relevant"] == True].copy()
