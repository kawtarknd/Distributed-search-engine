import csv
import json

# Ouvre le fichier CSV
with open('C:/Users/lenovo/Desktop/M1/M1 S2/systRetD/Projet/moteur-recherche-distribue/logstash/data/ai_projects.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    json_data = []

    for row in reader:
        json_entry = {
            "title": row["project_name"],
            "message": row["description"],
            "url": row["url"]
        }
        json_data.append(json_entry)

with open('projets2_ai.json', 'w', encoding='utf-8') as jsonfile:
    for entry in json_data:
        jsonfile.write(json.dumps(entry, ensure_ascii=False) + '\n')
