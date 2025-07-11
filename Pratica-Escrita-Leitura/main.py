# ==================================================
# BLOCO 1: ARQUIVOS TXT (15 exercícios)
# ==================================================

# --- Introdução ---
# Para arquivos TXT, usamos funções nativas do Python: open(), read(), write(), close()

# Exercício 1.1 (Resolvido)
# Crie um arquivo 'diario.txt' e registre uma entrada de diário sobre seu dia.
print("=" * 60)
print("EXERCÍCIO 1.1 - CRIANDO ARQUIVO DIÁRIO")
print("=" * 60)

with open('diario.txt', 'w', encoding='utf-8') as file:
    file.write("Hoje aprendi a manipular arquivos em Python!\n")
print("Arquivo 'diario.txt' criado com sucesso!")

# Exercício 1.2
# Crie um arquivo 'tarefas.txt' e adicione 3 tarefas diárias.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.2 - CRIANDO ARQUIVO TAREFAS")
print("=" * 60)

with open('tarefas.txt', 'w', encoding='utf-8') as file:
    file.write("Lavar a louça")
    file.write("\nFazer Faxina")
    file.write("\nPreparar a comida")
print("Arquivo 'tarefas.txt' criado com sucesso!")

# Exercício 1.3
# Crie um arquivo 'metas.txt' registrando 2 metas pessoais para o ano.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.3 - CRIANDO ARQUIVO METAS")
print("=" * 60)

with open('metas.txt', 'w', encoding='utf-8') as file:
    file.write("Viajar de avião")
    file.write("\nIr em um show de Coldplay")
print("Arquivo 'metas.txt' criado com sucesso!")

# Exercício 1.4 (Resolvido)
# Leia o conteúdo do arquivo 'diario.txt' e imprima na tela.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.4 - LENDO ARQUIVO DIÁRIO")
print("=" * 60)

with open('diario.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()
    print(conteudo)

# Exercício 1.5
# Leia o arquivo 'tarefas.txt' e mostre cada tarefa com um número de prefixo.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.5 - LISTA DE TAREFAS")
print("=" * 60)

with open('tarefas.txt', 'r', encoding='utf-8') as file:
    x=0
    for line in file:
        x+=1
        print(f"{x}. {line.strip()}")

# Exercício 1.6
# Leia 'metas.txt' e formate a saída com um '-' no começo de cada linha.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.6 - LISTA DE METAS")
print("=" * 60)

with open('metas.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():
            print(f"- {line.strip()}")

# Exercício 1.7 (Resolvido)
# Adicione uma nova linha ao final do 'diario.txt' sem apagar o conteúdo existente.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.7 - ADICIONANDO AO DIÁRIO")
print("=" * 60)

with open('diario.txt', 'a', encoding='utf-8') as file:
    file.write("Agora estou praticando escrita de arquivos!\n")
print("Nova linha adicionada ao diário!")

# Exercício 1.8
# Adicione uma nova tarefa ao 'tarefas.txt' sem apagar as existentes.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.8 - ADICIONANDO NOVA TAREFA")
print("=" * 60)

with open('tarefas.txt', 'a', encoding='utf-8') as file:
    file.write("\nArrumar o armário")
print("Nova tarefa adicionada!")

# Exercício 1.9
# Registre o progresso de uma meta no 'metas.txt'.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.9 - ATUALIZANDO PROGRESSO DAS METAS")
print("=" * 60)

with open('metas.txt', 'a', encoding='utf-8') as file:
    file.write("\nFalta pouco tempo para eu conseguir ir em um show de Coldplay")
print("Progresso registrado!")

# Exercício 1.10 (Resolvido)
# Conte quantas linhas existem no arquivo 'diario.txt'.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.10 - CONTANDO LINHAS DO DIÁRIO")
print("=" * 60)

with open('diario.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()
    print(f"Total de entradas no diário: {len(linhas)}")

# Exercício 1.11
# Conte quantas tarefas estão registradas em 'tarefas.txt'.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.11 - CONTANDO TAREFAS")
print("=" * 60)

with open('tarefas.txt', 'r', encoding='utf-8') as file:
    tarefas = file.readlines()
    print(f"Total de tarefas: {len(tarefas)}")

# Exercício 1.12
# Verifique se a palavra "urgente" aparece em qualquer tarefa.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.12 - VERIFICANDO TAREFAS URGENTES")
print("=" * 60)

urgente_encontrada = False
for tarefa in tarefas:
    if "urgente" in tarefa.lower():
        print(f"Tarefa urgente encontrada: {tarefa.strip()}")
        urgente_encontrada = True
if not urgente_encontrada:
    print("Nenhuma tarefa urgente encontrada.")

# Exercício 1.13 (Resolvido)
# Crie um backup do diário chamado 'diario_backup.txt'.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.13 - CRIANDO BACKUP DO DIÁRIO")
print("=" * 60)

with open('diario.txt', 'r', encoding='utf-8') as origem, open('diario_backup.txt', 'w', encoding='utf-8') as destino:
    destino.write(origem.read())
print("Backup do diário criado!")

# Exercício 1.14
# Crie um backup das tarefas com data no nome do arquivo.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.14 - CRIANDO BACKUP DAS TAREFAS")
print("=" * 60)

from datetime import datetime

data_atual = datetime.now().strftime("%Y-%m-%d")
with open('tarefas.txt', 'r', encoding='utf-8') as origem, open(f'tarefas_backup_{data_atual}.txt', 'w', encoding='utf-8') as destino:
    destino.write(origem.read())
print(f"Backup das tarefas criado: tarefas_backup_{data_atual}.txt")

# Exercício 1.15
# Transforme todas as metas em maiúsculas em um novo arquivo 'metas_prioridade.txt'.
print("\n" + "=" * 60)
print("EXERCÍCIO 1.15 - CRIANDO METAS PRIORITÁRIAS")
print("=" * 60)

with open('metas.txt', 'r', encoding='utf-8') as origem, open('metas_prioridade.txt', 'w', encoding='utf-8') as destino:
    for linha in origem:
        destino.write(linha.upper())
print("Arquivo 'metas_prioridade.txt' criado com metas em maiúsculas!")

# ==================================================
# BLOCO 2: ARQUIVOS CSV (15 exercícios)
# ==================================================

# --- Introdução ---
print("\n" + "=" * 60)
print("INICIANDO EXERCÍCIOS CSV")
print("=" * 60)
import csv

# Exercício 2.1 (Resolvido)
# Crie um arquivo 'contatos.csv' com cabeçalhos: nome,email,telefone
print("\n" + "=" * 60)
print("EXERCÍCIO 2.1 - CRIANDO ARQUIVO CONTATOS")
print("=" * 60)

cabecalhos = ['nome', 'email', 'telefone']
contatos = [
    ['Ana Silva', 'ana@email.com', '(11) 91234-5678'],
    ['Carlos Oliveira', 'carlos@empresa.com', '(21) 99876-5432']
]

with open('contatos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalhos)
    writer.writerows(contatos)
print("Arquivo 'contatos.csv' criado!")

# Exercício 2.2
# Crie um CSV 'produtos.csv' com campos: id,nome,preço,estoque
print("\n" + "=" * 60)
print("EXERCÍCIO 2.2 - CRIANDO ARQUIVO PRODUTOS")
print("=" * 60)

campos = ['id', 'nome', 'preço', 'estoque']
produtos = [
    ['1', 'sabonete', 2.00, 40],
    ['2', 'shampoo', 10.00, 70],
    ['3', 'condicionador', 8.00, 70]
]

with open('produtos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(campos)
    writer.writerows(produtos)
print("Arquivo 'produtos.csv' criado!")

# Exercício 2.3
# Crie um CSV 'eventos.csv' para registrar shows: artista,local,data,ingressos
print("\n" + "=" * 60)
print("EXERCÍCIO 2.3 - CRIANDO ARQUIVO EVENTOS")
print("=" * 60)

shows = ['artista', 'local', 'data', 'ingressos']
eventos = [
    ['Skank', 'Recife', '25/07/2025', 150],
    ['Coldplay', 'Recife', '31/07/2025', 1000],
    ['Ariana Grande', 'Recife', '17/02/2026', 700]
]

with open('eventos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(shows)
    writer.writerows(eventos)
print("Arquivo 'eventos.csv' criado!")

# Exercício 2.4 (Resolvido)
# Leia 'contatos.csv' e mostre os dados em formato de tabela
print("\n" + "=" * 60)
print("EXERCÍCIO 2.4 - LENDO CONTATOS EM FORMATO TABELA")
print("=" * 60)

with open('contatos.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for linha in reader:
        print(f"{linha[0]:<20} | {linha[1]:<20} | {linha[2]}")

# Exercício 2.5
# Leia 'produtos.csv' e calcule o valor total do estoque
print("\n" + "=" * 60)
print("EXERCÍCIO 2.5 - CALCULANDO VALOR TOTAL DO ESTOQUE")
print("=" * 60)

with open('produtos.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  
    
    valor_total_estoque = 0
    for linha in reader:
        valor_produto = float(linha[2])  
        qtd_produto = int(linha[3])      
        valor_total_estoque += valor_produto * qtd_produto
    print(f"O valor total do estoque é R${valor_total_estoque:.2f}")

# Exercício 2.6
# Leia 'eventos.csv' e mostre apenas eventos com ingressos disponíveis
print("\n" + "=" * 60)
print("EXERCÍCIO 2.6 - EVENTOS COM INGRESSOS DISPONÍVEIS")
print("=" * 60)

with open('eventos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for evento in reader:
        if int(evento['ingressos']) > 0:
            print(f"Evento disponível: {evento['artista']} em {evento['local']}")

# Exercício 2.7 (Resolvido)
# Adicione um novo contato ao 'contatos.csv'
print("\n" + "=" * 60)
print("EXERCÍCIO 2.7 - ADICIONANDO NOVO CONTATO")
print("=" * 60)

novo_contato = ['Maria Santos', 'maria@tech.com', '(31) 94567-1234']
with open('contatos.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(novo_contato)
print("Novo contato adicionado!")

# Exercício 2.8
# Adicione 3 novos produtos ao 'produtos.csv'
print("\n" + "=" * 60)
print("EXERCÍCIO 2.8 - ADICIONANDO NOVOS PRODUTOS")
print("=" * 60)

novos_produtos = [
    ['4', 'sabão em pó', 12.00, 30],
    ['5', 'detergente', 5.00, 50],
    ['6', 'amaciante', 8.00, 20]
]

with open('produtos.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(novos_produtos)
print("Novos produtos adicionados!")

# Exercício 2.9
# Registre um novo show no 'eventos.csv'
print("\n" + "=" * 60)
print("EXERCÍCIO 2.9 - REGISTRANDO NOVO SHOW")
print("=" * 60)

novo_show = ['Gorillaz', 'Recife', '10/10/2025', 200]
with open('eventos.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(novo_show)
print("Novo show registrado!")

# Exercício 2.10 (Resolvido)
# Converta o CSV para dicionário e encontre contatos com domínio específico
print("\n" + "=" * 60)
print("EXERCÍCIO 2.10 - BUSCANDO CONTATOS CORPORATIVOS")
print("=" * 60)

with open('contatos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if 'empresa.com' in contato['email']:
            print(f"Contato corporativo: {contato['nome']}")

# Exercício 2.11
# Calcule a média de preços dos produtos usando dicionários
print("\n" + "=" * 60)
print("EXERCÍCIO 2.11 - CALCULANDO MÉDIA DE PREÇOS")
print("=" * 60)

try:
    with open('produtos.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        total_preco = 0
        total_produtos = 0
        
        for produto in reader:
            try:
                total_preco += float(produto['preço'])
                total_produtos += 1
            except ValueError:
                print(f"Preço inválido encontrado: {produto['preço']}")
        
        if total_produtos > 0:
            media_preco = total_preco / total_produtos
            print(f"Média de preços dos produtos: R${media_preco:.2f}")
        else:
            print("Nenhum produto encontrado.")
except FileNotFoundError:
    print("Arquivo produtos.csv não encontrado.")
except KeyError:
    print("Coluna 'preço' não encontrada no arquivo CSV.")

# Exercício 2.12
# Atualize a quantidade de ingressos para um evento específico
print("\n" + "=" * 60)
print("EXERCÍCIO 2.12 - ATUALIZANDO INGRESSOS")
print("=" * 60)

with open('eventos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    eventos = list(reader)
    
for evento in eventos:
    if evento['artista'] == 'Gorillaz':
        evento['ingressos'] = '0'
        print(f"Ingressos do show {evento['artista']} esgotados!")

# Exercício 2.13 (Resolvido)
# Valide telefones no formato (XX) XXXXX-XXXX
print("\n" + "=" * 60)
print("EXERCÍCIO 2.13 - VALIDANDO TELEFONES")
print("=" * 60)

import re
telefones_validos = True
with open('contatos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if not re.match(r'\(\d{2}\) \d{5}-\d{4}', contato['telefone']):
            print(f"Telefone inválido: {contato['nome']}")
            telefones_validos = False
if telefones_validos:
    print("Todos os telefones estão no formato correto!")

# Exercício 2.14
# Valide se todos os IDs de produtos são únicos
print("\n" + "=" * 60)
print("EXERCÍCIO 2.14 - VALIDANDO IDS ÚNICOS")
print("=" * 60)

with open('produtos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    ids_produtos = set()
    ids_duplicados = False
    for produto in reader:
        if produto['id'] in ids_produtos:
            print(f"ID duplicado encontrado: {produto['id']}")
            ids_duplicados = True
        else:
            ids_produtos.add(produto['id'])
    if not ids_duplicados:
        print("Todos os IDs são únicos!")

# Exercício 2.15
# Crie um sistema de busca por artista no 'eventos.csv'
print("\n" + "=" * 60)
print("EXERCÍCIO 2.15 - SISTEMA DE BUSCA POR ARTISTA")
print("=" * 60)

def buscar_artista(nome_artista):
    with open('eventos.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        encontrado = False
        for evento in reader:
            if nome_artista.lower() in evento['artista'].lower():
                print(f"Evento encontrado: {evento['artista']} em {evento['local']} na data {evento['data']}")
                encontrado = True
        if not encontrado:
            print(f"Nenhum evento encontrado para: {nome_artista}")

# Teste da função
buscar_artista("Coldplay")

# ==================================================
# BLOCO 3: ARQUIVOS JSON (15 exercícios) - TEMA: JOGOS E REDES SOCIAIS
# ==================================================

# --- Introdução ---
print("\n" + "=" * 60)
print("INICIANDO EXERCÍCIOS JSON")
print("=" * 60)
import json

# Exercício 3.1 (Resolvido)
# Salve os dados de um personagem de RPG em 'personagem.json'
print("\n" + "=" * 60)
print("EXERCÍCIO 3.1 - CRIANDO PERSONAGEM RPG")
print("=" * 60)

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
print("Personagem criado e salvo!")

# Exercício 3.2
# Crie um arquivo 'perfil_instagram.json' com dados de um influenciador
print("\n" + "=" * 60)
print("EXERCÍCIO 3.2 - CRIANDO PERFIL INSTAGRAM")
print("=" * 60)

perfil_instagram = {
    "username": "Luisa",
    "seguidores": 5000,
    "seguindo": 100,
    "posts": 50,
    "likes": 2500,
    "biografia": "Sejam bem-vindos ao meu perfil!"
}

with open('perfil_instagram.json', 'w', encoding='utf-8') as file:
    json.dump(perfil_instagram, file, indent=4)
print("Perfil Instagram criado!")

# Exercício 3.3
# Armazene os dados de um monstro em 'monstro.json'
print("\n" + "=" * 60)
print("EXERCÍCIO 3.3 - CRIANDO MONSTRO")
print("=" * 60)

monstro = {
    "nome": "Dragão de Fogo",
    "tipo": "Fogo",
    "nivel": 20,
    "pontos_ataque": 150,
    "recompensas": [
        {"nome": "Ouro", "valor": 100},
        {"nome": "Escama de Dragão", "valor": 500},
        {"nome": "Poção de Fogo", "valor": 250}
    ]
}

with open('monstro.json', 'w') as file:
    json.dump(monstro, file, indent=4)
print("Monstro criado!")

# Exercício 3.4 (Resolvido)
# Leia 'personagem.json' e mostre as habilidades do personagem
print("\n" + "=" * 60)
print("EXERCÍCIO 3.4 - LENDO HABILIDADES DO PERSONAGEM")
print("=" * 60)

with open('personagem.json') as file:
    dados = json.load(file)
    print("Habilidades:", ", ".join(dados['habilidades']))

# Exercício 3.5
# Leia 'perfil_instagram.json' e calcule a taxa de engajamento
print("\n" + "=" * 60)
print("EXERCÍCIO 3.5 - CALCULANDO TAXA DE ENGAJAMENTO")
print("=" * 60)

with open('perfil_instagram.json') as file:
    dados = json.load(file)
    taxa_engajamento = dados['likes'] / dados['posts'] if dados['posts'] > 0 else 0
    print(f"Taxa de engajamento: {taxa_engajamento:.2f} likes por post")

# Exercício 3.6
# Leia 'monstro.json' e mostre a recompensa mais valiosa
print("\n" + "=" * 60)
print("EXERCÍCIO 3.6 - RECOMPENSA MAIS VALIOSA")
print("=" * 60)

with open('monstro.json') as file:
    dados = json.load(file)
    recompensa_mais_valiosa = max(dados['recompensas'], key=lambda x: x['valor'])
    print("Recompensa mais valiosa:", recompensa_mais_valiosa['nome'])

# Exercício 3.7 (Resolvido)
# Atualize o nível do personagem para 16 e salve no arquivo
print("\n" + "=" * 60)
print("EXERCÍCIO 3.7 - ATUALIZANDO NÍVEL DO PERSONAGEM")
print("=" * 60)

with open('personagem.json') as file:
    dados = json.load(file)
    
dados['nivel'] = 16

with open('personagem.json', 'w') as file:
    json.dump(dados, file, indent=4)
print("Nível do personagem atualizado para 16!")

# Exercício 3.8
# Adicione um novo post ao perfil do Instagram
print("\n" + "=" * 60)
print("EXERCÍCIO 3.8 - ADICIONANDO NOVO POST")
print("=" * 60)

novo_post = {
    "data": "2023-10-01",
    "likes": 150
}

with open('perfil_instagram.json') as file:
    dados = json.load(file)
    dados['posts'] += 1
    dados['likes'] += novo_post['likes']

with open('perfil_instagram.json', 'w') as file:
    json.dump(dados, file, indent=4)
print("Novo post adicionado ao perfil!")

# Exercício 3.9
# Atualize os pontos de ataque do monstro após uma evolução
print("\n" + "=" * 60)
print("EXERCÍCIO 3.9 - EVOLUINDO MONSTRO")
print("=" * 60)

with open('monstro.json') as file:
    dados = json.load(file)
    dados['pontos_ataque'] += 20

with open('monstro.json', 'w') as file:
    json.dump(dados, file, indent=4)
print("Monstro evoluído! Pontos de ataque aumentados!")

# Exercício 3.10 (Resolvido)
# Valide se o personagem tem equipamento de arma
print("\n" + "=" * 60)
print("EXERCÍCIO 3.10 - VALIDANDO EQUIPAMENTO DO PERSONAGEM")
print("=" * 60)

with open('personagem.json') as file:
    dados = json.load(file)
    if "arma" in dados['equipamentos'] and dados['equipamentos']['arma'] != "Nenhum":
        print("Personagem está armado!")
    else:
        print("Personagem desarmado!")

# Exercício 3.11
# Verifique se o perfil do Instagram tem mais de 10.000 seguidores
print("\n" + "=" * 60)
print("EXERCÍCIO 3.11 - VERIFICANDO POPULARIDADE DO PERFIL")
print("=" * 60)

with open('perfil_instagram.json') as file:
    dados = json.load(file)
    if dados['seguidores'] > 10000:
        print("Perfil com mais de 10.000 seguidores!")
    else:
        print("Perfil com menos de 10.000 seguidores.")

# Exercício 3.12
# Calcule o valor total das recompensas do monstro
print("\n" + "=" * 60)
print("EXERCÍCIO 3.12 - CALCULANDO VALOR TOTAL DAS RECOMPENSAS")
print("=" * 60)

with open('monstro.json') as file:
    dados = json.load(file)
    valor_total = sum(item['valor'] for item in dados['recompensas'])
    print("Valor total das recompensas:", valor_total)

# Exercício 3.13 (Resolvido)
# Converta os dados do personagem para string JSON e salve em formato minificado
print("\n" + "=" * 60)
print("EXERCÍCIO 3.13 - CRIANDO VERSÃO MINIFICADA")
print("=" * 60)

personagem_str = json.dumps(personagem, separators=(',', ':'))
with open('personagem_min.json', 'w') as file:
    file.write(personagem_str)
print("Versão minificada criada!")

# Exercício 3.14
# Crie um backup do perfil do Instagram com a data atual no nome do arquivo
print("\n" + "=" * 60)
print("EXERCÍCIO 3.14 - CRIANDO BACKUP DO PERFIL")
print("=" * 60)

import datetime
data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
with open('perfil_instagram.json') as file:
    dados = json.load(file)

with open(f'perfil_instagram_backup_{data_atual}.json', 'w') as file:
    json.dump(dados, file, indent=4)
print(f"Backup criado: perfil_instagram_backup_{data_atual}.json")

# Exercício 3.15
# Combine dados de múltiplos personagens em um arquivo 'grupo.json'
print("\n" + "=" * 60)
print("EXERCÍCIO 3.15 - CRIANDO GRUPO DE PERSONAGENS")
print("=" * 60)

# First, create a second character
personagem2 = {
    "nome": "Jon Snow",
    "nivel": 18,
    "hp": 400,
    "habilidades": ["Combate", "Liderança", "Resistência"],
    "equipamentos": {
        "arma": "Longclaw",
        "armadura": "Couro Negro",
        "anel": "Nenhum"
    }
}

with open('personagem2.json', 'w') as file:
    json.dump(personagem2, file, indent=4)

with open('personagem.json') as file:
    personagem = json.load(file)

with open('personagem2.json') as file:
    personagem2 = json.load(file)

grupo = {
    "personagens": [personagem, personagem2]
}

with open('grupo.json', 'w') as file:
    json.dump(grupo, file, indent=4)
print("Grupo de personagens criado!")

# ==================================================
# BLOCO 4: EXERCÍCIOS MISTOS (5 exercícios)
# ==================================================

print("\n" + "=" * 60)
print("INICIANDO EXERCÍCIOS MISTOS")
print("=" * 60)

# Exercício 4.1 (Resolvido)
# Converta dados de personagens de JSON para CSV
print("\n" + "=" * 60)
print("EXERCÍCIO 4.1 - CONVERTENDO JSON PARA CSV")
print("=" * 60)

def json_para_csv(origem, destino):
    with open(origem) as json_file:
        dados = json.load(json_file)
    
    with open(destino, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dados.keys())
        writer.writerow(dados.values())

json_para_csv('personagem.json', 'personagem.csv')
print("Conversão JSON para CSV concluída!")

# Exercício 4.2
# Crie um sistema de inventário que salva itens em TXT, CSV e JSON
print("\n" + "=" * 60)
print("EXERCÍCIO 4.2 - SISTEMA DE INVENTÁRIO")
print("=" * 60)

inventario = {
    "itens": [
        {"nome": "Espada", "tipo": "arma", "nivel": 5},
        {"nome": "Poção de Vida", "tipo": "consumivel", "nivel": 1}
    ]
}

with open('inventario.json', 'w') as file:
    json.dump(inventario, file, indent=4)

with open('inventario.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(inventario['itens'][0].keys())
    for item in inventario['itens']:
        writer.writerow(item.values())

with open('inventario.txt', 'w', encoding='utf-8') as file:
    for item in inventario['itens']:
        file.write(f"Nome: {item['nome']}, Tipo: {item['tipo']}, Nível: {item['nivel']}\n")

print("Sistema de inventário criado em 3 formatos!")

# Exercício 4.3
# Desenvolva um feed de notícias de jogo que salva em JSON e exporta para TXT
print("\n" + "=" * 60)
print("EXERCÍCIO 4.3 - FEED DE NOTÍCIAS")
print("=" * 60)

feed_noticias = [
    {"titulo": "Novo evento de caça", "data": "2023-10-01", "conteudo": "Participe do evento de caça ao dragão!"},
    {"titulo": "Atualização de personagem", "data": "2023-10-02", "conteudo": "Agora você pode evoluir seu personagem para o nível 20!"}
]

with open('feed_noticias.json', 'w') as file:
    json.dump(feed_noticias, file, indent=4)

with open('feed_noticias.txt', 'w', encoding='utf-8') as file:
    for noticia in feed_noticias:
        file.write(f"{noticia['data']} - {noticia['titulo']}: {noticia['conteudo']}\n")

print("Feed de notícias criado!")

# Exercício 4.4
# Crie um analisador de perfil social que lê JSON e gera relatório em CSV
print("\n" + "=" * 60)
print("EXERCÍCIO 4.4 - ANALISADOR DE PERFIL SOCIAL")
print("=" * 60)

with open('perfil_instagram.json') as file:
    perfil = json.load(file)

with open('relatorio_perfil.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(perfil.keys())
    writer.writerow(perfil.values())

print("Relatório de perfil gerado!")

# Exercício 4.5
# Implemente um sistema de save game que compacta dados em ZIP
print("\n" + "=" * 60)
print("EXERCÍCIO 4.5 - SISTEMA DE SAVE GAME")
print("=" * 60)

import zipfile

def salvar_jogo_em_zip(arquivo_json, arquivo_zip):
    with zipfile.ZipFile(arquivo_zip, 'w') as zip_file:
        zip_file.write(arquivo_json)

salvar_jogo_em_zip('personagem.json', 'save_game.zip')
print("Save game compactado em ZIP!")

print("\n" + "=" * 60)
print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")
print("=" * 60)