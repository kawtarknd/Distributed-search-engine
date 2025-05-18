from flask import Blueprint, render_template, request
from elastic_client import get_client

es = get_client()
routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
@routes.route("/search", methods=["GET", "POST"])
def search():
    results = []
    index_name = "*"
    query = request.form.get("query") or request.args.get("query")
    tag = request.args.get("tag")

    if tag:
        body = {
            "query": {
                "term": {
                    "tags.keyword": tag
                }
            }
        }
    elif query:
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "source", "message", "tags"]
                }
            }
        }
    else:
        # Aucun tag ni mot-clé => ne fais pas de requête
        return render_template("search.html", results=[])

    try:
        response = es.search(index=index_name, body=body)
        results = response["hits"]["hits"]
    except Exception as e:
        results = [{"_source": {"title": "Erreur", "source": "", "date": "", "message": str(e)}}]

    return render_template("search.html", results=results)


@routes.route("/about")
def about():
    return render_template("about.html")

@routes.route("/ping")
def ping():
    if es.ping():
        return "✅ Elasticsearch connecté"
    return "❌ Problème de connexion à Elasticsearch", 500
