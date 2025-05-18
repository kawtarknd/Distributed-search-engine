import requests
from elastic_client import get_client

es = get_client()

# API Hacker News via Algolia
url = "https://hn.algolia.com/api/v1/search?query=AI"

# Requête
response = requests.get(url)
data = response.json()

# Création de l'index (si pas encore existant)
index_name = "hn_ai_articles"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Insertion des documents
for item in data.get("hits", []):
    doc = {
        "title": item.get("title") or item.get("story_title") or "Sans titre",
        "source": "Hacker News",
        "date": item.get("created_at", "")[:10],
        "message": item.get("story_text") or item.get("comment_text") or "",
        "url": item.get("url") or item.get("story_url") or f"https://news.ycombinator.com/item?id={item['objectID']}",
        "tags": ["hackernews", "tech", "AI"]
    }

    es.index(index=index_name, document=doc)

print(f"✅ Données importées dans l'index : {index_name}")
