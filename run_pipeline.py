from src.identification import identify_people
from src.enrichment import enrich_people
from src.ranking import rank_and_export

people = identify_people("data/raw/people_profiles.csv")
enriched = enrich_people(people)
final = rank_and_export(enriched)

print("Pipeline executed successfully")
