import csv
import json

# Chemin du fichier CSV en entrée
csv_path = 'C:/Users/lenovo/Desktop/M1/M1 S2/systRetD/Projet/moteur-recherche-distribue/logstash/data/Data Breaches.csv'

# Chemin du fichier JSON en sortie
output_path = 'data_breaches_array.json'

json_data = []

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        json_entry = {
            "title": row["Entity"],
            "source": row["Sources name"] or "Unknown",
            "date": row["Year"] or "Unknown",
            "message": row["Description"],
            "tags": [row["Target Organization Type"], row["Method of Leak"]],
            "url": row["Sources Link"]
        }
        json_data.append(json_entry)

# Écriture dans un tableau JSON
with open(output_path, 'w', encoding='utf-8') as jsonfile:
    for entry in json_data:
        jsonfile.write(json.dumps(entry, ensure_ascii=False) + '\n')


