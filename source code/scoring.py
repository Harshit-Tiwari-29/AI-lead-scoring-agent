BIOTECH_HUBS = ["boston", "cambridge", "basel", "san diego"]

def calculate_score(row):
    score = 0

    # Role relevance
    score += 30

    # Funding signal
    if row["funding_stage"] in ["Series A", "Series B", "Series C"]:
        score += 20

    # Research intent
    if row["recent_research"] == 1:
        score += 40

    # Location hub
    if row["person_location"].lower() in BIOTECH_HUBS:
        score += 10

    return min(score, 100)
