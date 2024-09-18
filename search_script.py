import requests
import json
import urllib.parse

API_KEY = 'SUA_CHAVE_API'  # Substitua com sua chave de API
CX = 'SEU_CX'  # Substitua com seu ID do mecanismo de pesquisa personalizado

queries = [
    'editais para projetos sociais em aberto',
    'editais para projetos de inovação em aberto',
    'editais projetos para leis de incentivo',
    'editais de licitação para projetos'
]

num_results = 10

results = {}

def search_and_save_results(query):
    try:
        encoded_query = urllib.parse.quote_plus(query)
        url = f'https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={API_KEY}&cx={CX}&num={num_results}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results[query] = data.get('items', [])
        else:
            results[query] = []
    except Exception as e:
        results[query] = []

for query in queries:
    search_and_save_results(query)

with open('search_results.json', 'w') as f:
    json.dump(results, f)
