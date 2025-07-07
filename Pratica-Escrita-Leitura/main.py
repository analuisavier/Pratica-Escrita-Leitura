# ==================================================
# BLOCO 1: ARQUIVOS TXT (15 exercícios)
# ==================================================

# --- Introdução ---
# Para arquivos TXT, usamos funções nativas do Python: open(), read(), write(), close()

# Exercício 1.1 (Resolvido)
# Crie um arquivo 'diario.txt' e registre uma entrada de diário sobre seu dia.

with open('diario.txt', 'w', encoding='utf-8') as file:
    file.write("Hoje aprendi a manipular arquivos em Python!\n")

# Exercício 1.2
# Crie um arquivo 'tarefas.txt' e adicione 3 tarefas diárias.

with open('tarefas.txt', 'w', encoding='utf-8') as file:
    file.write("Lavar a louça")
    file.write("\nFazer Faxina")
    file.write("\nPreparar a comida")

# Exercício 1.3
# Crie um arquivo 'metas.txt' registrando 2 metas pessoais para o ano.

with open('metas.txt', 'w', encoding='utf-8') as file:
    file.write("\nViajar de avião")
    file.write("\nIr em um show de Coldplay")

# Exercício 1.4 (Resolvido)
# Leia o conteúdo do arquivo 'diario.txt' e imprima na tela.

with open('diario.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Exercício 1.5
# Leia o arquivo 'tarefas.txt' e mostre cada tarefa com um número de prefixo.

with open('tarefas.txt', 'r') as file:
    x=0
    for line in file:
        x+=1
        print(f"{x}. {line.strip()}")

# Exercício 1.6
# Leia 'metas.txt' e formate a saída com um '-' no começo de cada linha.

with open('metas.txt', 'r') as file:
    linhas = file.readlines()
    for line in file:
        print(f" - {line.strip()}")

# Exercício 1.7 (Resolvido)
# Adicione uma nova linha ao final do 'diario.txt' sem apagar o conteúdo existente.
with open('diario.txt', 'a') as file:
    file.write("Agora estou praticando escrita de arquivos!\n")

# Exercício 1.8
# Adicione uma nova tarefa ao 'tarefas.txt' sem apagar as existentes.

with open('tarefas.txt', 'a', encoding='utf-8') as file:
    file.write("\nArrumar o armário")

# Exercício 1.9
# Registre o progresso de uma meta no 'metas.txt'.

with open('metas.txt', 'a', encoding='utf-8') as file:
    file.write("\nFalta pouco tempo para eu conseguir ir em um show de Coldplay")

# Exercício 1.10 (Resolvido)
# Conte quantas linhas existem no arquivo 'diario.txt'.
with open('diario.txt', 'r') as file:
    linhas = file.readlines()
    print(f"Total de entradas no diário: {len(linhas)}")

# Exercício 1.11
# Conte quantas tarefas estão registradas em 'tarefas.txt'.



# Exercício 1.12
# Verifique se a palavra "urgente" aparece em qualquer tarefa.

# Exercício 1.13 (Resolvido)
# Crie um backup do diário chamado 'diario_backup.txt'.
with open('diario.txt', 'r') as origem, open('diario_backup.txt', 'w') as destino:
    destino.write(origem.read())

# Exercício 1.14
# Crie um backup das tarefas com data no nome do arquivo.

# Exercício 1.15
# Transforme todas as metas em maiúsculas em um novo arquivo 'metas_prioridade.txt'.

# ==================================================
# BLOCO 2: ARQUIVOS CSV (15 exercícios)
# ==================================================

# --- Introdução ---
import csv

# Exercício 2.1 (Resolvido)
# Crie um arquivo 'contatos.csv' com cabeçalhos: nome,email,telefone
cabecalhos = ['nome', 'email', 'telefone']
contatos = [
    ['Ana Silva', 'ana@email.com', '(11) 91234-5678'],
    ['Carlos Oliveira', 'carlos@empresa.com', '(21) 99876-5432']
]

with open('contatos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalhos)
    writer.writerows(contatos)

# Exercício 2.2
# Crie um CSV 'produtos.csv' com campos: id,nome,preço,estoque

campos = ['id', 'nome', 'preço', 'estoque']
produtos = [
    ['1', 'sabonete', 2,00, 40],
    ['2', 'shampoo', 10,00, 70],
    ['3', 'condicionador', 8,00, 70]
]

with open('produtos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(campos)
    writer.writerows(produtos)

# Exercício 2.3
# Crie um CSV 'eventos.csv' para registrar shows: artista,local,data,ingressos

shows = ['artista', 'local', 'data', 'ingressos']
eventos = [
    ['Skank', 'Mineirão', '25/07/2025', 150],
    ['Coldplay', 'Rio de Janeiro', '15/09/2025', 1000],
    ['Ariana Grande', 'Recife', '17/02/2026', 700]
]

# Exercício 2.4 (Resolvido)
# Leia 'contatos.csv' e mostre os dados em formato de tabela
with open('contatos.csv', newline='') as file:
    reader = csv.reader(file)
    for linha in reader:
        print(f"{linha[0]:<20} | {linha[1]:<20} | {linha[2]}")

# Exercício 2.5
# Leia 'produtos.csv' e calcule o valor total do estoque

with open('produtos.csv', newline='') as file:
    reader = csv.reader(file)
    valor_total_estoque = 0
    for linha in reader:
        valor_produto = linha[2]
        qtd_produto = linha[3]
        valor_total_estoque += valor_produto * qtd_produto
    print(f"O valor total do estoque é R${valor_total_estoque}")    


# Exercício 2.6
# Leia 'eventos.csv' e mostre apenas eventos com ingressos disponíveis

# Exercício 2.7 (Resolvido)
# Adicione um novo contato ao 'contatos.csv'
novo_contato = ['Maria Santos', 'maria@tech.com', '(31) 94567-1234']
with open('contatos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_contato)

# Exercício 2.8
# Adicione 3 novos produtos ao 'produtos.csv'

# Exercício 2.9
# Registre um novo show no 'eventos.csv'

# Exercício 2.10 (Resolvido)
# Converta o CSV para dicionário e encontre contatos com domínio específico
with open('contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if 'empresa.com' in contato['email']:
            print(f"Contato corporativo: {contato['nome']}")

# Exercício 2.11
# Calcule a média de preços dos produtos usando dicionários

# Exercício 2.12
# Atualize a quantidade de ingressos para um evento específico

# Exercício 2.13 (Resolvido)
# Valide telefones no formato (XX) XXXXX-XXXX
import re
with open('contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if not re.match(r'\(\d{2}\) \d{5}-\d{4}', contato['telefone']):
            print(f"Telefone inválido: {contato['nome']}")

# Exercício 2.14
# Valide se todos os IDs de produtos são únicos

# Exercício 2.15
# Crie um sistema de busca por artista no 'eventos.csv'

# ==================================================
# ==================================================
# BLOCO 3: ARQUIVOS JSON (15 exercícios) - TEMA: JOGOS E REDES SOCIAIS
# ==================================================

# --- Introdução ---
import json

# Exercício 3.1 (Resolvido)
# Salve os dados de um personagem de RPG em 'personagem.json': nome, nível, pontos de vida, habilidades e equipamentos
personagem = {
    "nome": "Arya Stark",
    "nivel": 15,
    "hp": 320,
    "habilidades": ["Agilidade", "Furtividade", "Disfarces"],
    "equipamentos": {
        "arma": "Agulha",
        "armadura": "Couro",
        "anel": "Nenhum"
    }
}

with open('personagem.json', 'w') as file:
    json.dump(personagem, file, indent=4)

# Exercício 3.2
# Crie um arquivo 'perfil_instagram.json' com dados de um influenciador: username, seguidores, seguindo, posts e biografia

perfil_instagram = {
    "username": "Luísa",
    "seguidores": 5.000,
    "seguindo": 100,
    "posts": 50,
    "biografia":  
}

# Exercício 3.3
# Armazene os dados de um monstro em 'monstro.json': nome, tipo, nível, pontos_ataque e recompensas

# Exercício 3.4 (Resolvido)
# Leia 'personagem.json' e mostre as habilidades do personagem
with open('personagem.json') as file:
    dados = json.load(file)
    print("Habilidades:", ", ".join(dados['habilidades']))

# Exercício 3.5
# Leia 'perfil_instagram.json' e calcule a taxa de engajamento (média de likes por post)

# Exercício 3.6
# Leia 'monstro.json' e mostre a recompensa mais valiosa

# Exercício 3.7 (Resolvido)
# Atualize o nível do personagem para 16 e salve no arquivo
with open('personagem.json') as file:
    dados = json.load(file)
    
dados['nivel'] = 16

with open('personagem.json', 'w') as file:
    json.dump(dados, file, indent=4)

# Exercício 3.8
# Adicione um novo post ao perfil do Instagram com data e likes

# Exercício 3.9
# Atualize os pontos de ataque do monstro após uma evolução

# Exercício 3.10 (Resolvido)
# Valide se o personagem tem equipamento de arma
with open('personagem.json') as file:
    dados = json.load(file)
    if "arma" in dados['equipamentos'] and dados['equipamentos']['arma']:
        print("Personagem está armado!")
    else:
        print("Personagem desarmado!")

# Exercício 3.11
# Verifique se o perfil do Instagram tem mais de 10.000 seguidores

# Exercício 3.12
# Calcule o valor total das recompensas do monstro

# Exercício 3.13 (Resolvido)
# Converta os dados do personagem para string JSON e salve em formato minificado
personagem_str = json.dumps(personagem, separators=(',', ':'))
with open('personagem_min.json', 'w') as file:
    file.write(personagem_str)

# Exercício 3.14
# Crie um backup do perfil do Instagram com a data atual no nome do arquivo

# Exercício 3.15
# Combine dados de múltiplos personagens em um arquivo 'grupo.json'

# ==================================================
# BLOCO 4: EXERCÍCIOS MISTOS (5 exercícios)
# ==================================================

# Exercício 4.1 (Resolvido)
# Converta dados de personagens de JSON para CSV
def json_para_csv(origem, destino):
    with open(origem) as json_file:
        dados = json.load(json_file)
    
    with open(destino, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dados.keys())
        writer.writerow(dados.values())

# Teste:
json_para_csv('personagem.json', 'personagem.csv')

# Exercício 4.2
# Crie um sistema de inventário que salva itens coletados em TXT, CSV e JSON

# Exercício 4.3
# Desenvolva um feed de notícias de jogo que salva em JSON e exporta para TXT

# Exercício 4.4
# Crie um analisador de perfil social que lê JSON e gera relatório em CSV

# Exercício 4.5
# Implemente um sistema de save game que compacta dados em ZIP
