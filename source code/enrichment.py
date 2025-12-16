import pandas as pd

def enrich_people(people_df):
    pubs = pd.read_csv("data/raw/publications.csv")
    funding = pd.read_csv("data/raw/company_funding.csv")

    df = people_df.merge(pubs, on="person_id", how="left")
    df = df.merge(funding, on="company", how="left")

    df["recent_research"] = df["year"].apply(
        lambda x: 1 if x >= 2023 else 0
    )

    return df
