# São tipos especiais de iteradores, ao contrário das listas ou outros
# iteráveis, não armazenam todos os seus valores na memória
# São definidos usando funções regulares, mas, ao invés de retornar valores
# usando "return", utilizam "yield"

# Uma vez que um item gerado é consumido, ele é esquecido e não pode ser
# acessado novamente.

# O estado interno de um gerador é mantido entre chamadas

# A execução de um gerador é pausada na declaração "yield" e retormada daí
# na próxima vez que ele for chamado

import requests

def fetch_products(api_url, max_pages: int = 100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data["products"]:
            yield product
        if "next_page" not in data:
            break
        page +- 1

# Uso do gerador
# for product in fetch_products("http://api.example.com/products"):
#     print(product["name"])

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador([1, 2, 3]):
    print(i)