# Dicionário é um conjunto não-ordenado de pares chave:valor
# As chaves são únicas

pessoa = {"nome": "Charllie", "idade": 28}
pessoa = dict(nome="Charllie", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Charllie", "idade": 28, "telefone": "333-1234"}

# Os dados são acessados e modificados através da chave
dados = {"nome": "Challie", "idade": 30, "telefone": "3333-1234"}

dados["nome"] # "Charllie"
dados["idade"] # 30
dados["telefone"] # "3333-1234"

# Modificando valores 
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

# Dicionários aninhados
contatos = {
    "charllie@email.com": {"nome": "Charllie", "telefone": "3333-1234"},
    "caly@email.com": {"nome": "Caly", "telefone": "3333-1234"},
    "isa@email.com": {"nome": "Isa", "telefone": "3333-1234"}
}

contatos["charllie@email.com"]["telefone"] # "3333-1234"

# Iterando
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():  # Forma mais legível
    print(chave, valor)


# Métodos dicionário
copia = contatos.copy() # Cria um novo dicionário como cópia do primeiro
dict.fromkeys(["nome", "telefone"], "vazio") # cria chaves no dicionário com um valor padrão dict. uso o nome do dicionário.
dict.fromkeys(["nome", "telefone"]) # Cria chaves no dicionário sem valor padrão => no lugar do dict. uso o nome do dicionário.

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("charllie@email.com", {}) # "charllie@email.com": {"nome": "Charllie", "telefone": "3333-1234"}
contatos.items() # dict_items([("charllie@email.com": {"nome": "Charllie", "telefone": "3333-1234"})])
contatos.keys() # dict_keys(["charllie@email.com", "caly@email.com", "isa@email.com"])
contatos.pop("charllie@email.com") # "charllie@email.com": {"nome": "Charllie", "telefone": "3333-1234"}
contatos.pop("charllie@email.com", "Não encontrado") # "Não encontrado"
contatos.popitem() # Remove items em sequência
contatos.setdefault("nome", "Giovania") # Se o atributo(chave) estiver no dicionário, retorna ele, se não, insere ele
contatos.update({"camily@email.com": {"nome": "Camily"}}) # Atualiza o dicionário para os atributos aqui configurados
contatos.values() # Retorna todos os valores sem as chaves

"charllie@email.com" in contatos # True
"no@email.com" in contatos # False

del contatos["charllie@email.com"]["telefone"] # Remove o telefone da chave "charllie@email.com"
del contatos["charllie@email.com"] # Remove todo o conteúdo de chave "charllie@email.com"


