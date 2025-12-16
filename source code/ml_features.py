def create_ml_features(df):
    df = df.copy()

    df["senior_role"] = df["job_title"].str.lower().apply(
        lambda x: 1 if any(k in x for k in ["director", "vp", "head"]) else 0
    )

    df["funded_company"] = df["funding_stage"].apply(
        lambda x: 1 if x in ["Series A", "Series B", "Series C"] else 0
    )

    df["hub_location"] = df["person_location"].str.lower().apply(
        lambda x: 1 if x in ["boston", "cambridge", "basel", "san diego"] else 0
    )

    df["recent_research"] = df["recent_research"].fillna(0)

    return df
