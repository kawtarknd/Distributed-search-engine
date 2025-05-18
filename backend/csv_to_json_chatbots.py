import csv
import json

# Configuration personnalisée
conf = {
    "source": "ChatterbotCollection",
    "category": "AI Chatbots",
    "custom_note": "Imported with chatbot tag"
}

# Fichiers
csv_file = r"C:/Users/lenovo/Desktop/M1/M1 S2/systRetD/Projet/moteur-recherche-distribue/logstash/data/ChatterbotsDB.csv"
json_file = "chatbots_data.json"

with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    with open(json_file, mode='w', encoding='utf-8') as out:
        for row in reader:
            if not row.get("Name", "").strip():
                continue  # ignorer les lignes vides ou sans nom

            tags = [tag.strip() for tag in row.get("Tags", "").split(",") if tag.strip()]
            if "chatbots" not in [t.lower() for t in tags]:
                tags.append("chatbots")

            entry = {
                "title": row.get("Name", "").strip(),
                "image": row.get("Image", "").strip(),
                "description": row.get("Description", "").strip(),
                "language": row.get("Language", "").strip(),
                "homepage": row.get("Homepage", "").strip(),
                "profile": row.get("Profile", "").strip(),
                "year_submitted": row.get("Year Submitted", "").strip(),
                "year_launched": row.get("Year Launched", "").strip(),
                "tags": tags,
                "conf": conf
            }

            out.write(json.dumps(entry, ensure_ascii=False) + '\n')
