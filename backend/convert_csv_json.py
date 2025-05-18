import csv
import json
from pathlib import Path

# Chemin vers ton fichier CSV
CSV_PATH = Path(r"C:\Users\utilisateur\Desktop\Distributed-search-engine\logstash\data\Data Breaches.csv")

# Chemin du fichier JSON de sortie (même dossier, même nom mais extension .json)
NDJSON_OUT = CSV_PATH.with_suffix(".json")

# Colonnes à garder et leurs noms dans le JSON
COLUMN_MAP = {
    "Entity": "entity",
    "Description": "description",
    "Sources Link": "source_link",
    "Sources name": "source_name"
}

with CSV_PATH.open(encoding="utf-8") as f_in, NDJSON_OUT.open("w", encoding="utf-8") as f_out:
    reader = csv.DictReader(f_in)
    for row in reader:
        clean = {json_key: (row[csv_key].strip() or None) for csv_key, json_key in COLUMN_MAP.items()}
        f_out.write(json.dumps(clean, ensure_ascii=False) + "\n")

print(f"✅  Fichier NDJSON généré : {NDJSON_OUT}")

