from elasticsearch import Elasticsearch

def get_client():
    return Elasticsearch(
        "https://localhost:9200",
        http_auth=("elastic", "75+D3Nm2SA0rAueloxEU"),
        verify_certs=False  # ⚠️ True en production avec certificat valide
    )
