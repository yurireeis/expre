import re

#

text = """
Para entrar em contato r. Alagoas, 1049 5 e 6 andares
Savassi - Belo Horizonte MG Brasil
+55 (31) 3261-8083
contato@ancieladvogados.com.br
11/08/2016
para contato somente a partir das 18:00hrs
"""

"""
UTILIZANDO O METÓDO SEARCH
(retorna o match e os grupos)
"""
# usar o raw string para criar o padrão
# o search retorna na primeira ocorrência
# buscando pela primeira palavra que tenha a letra maiúscula
pattern = r'[A-Z]\w+'
match = re.search(pattern, text)
print(match)

# buscando pela primeira palavra que tenha apenas números
pattern = r'[0-9]\w+'
match = re.search(pattern, text)
print(match)

# buscando um telefone
pattern = r'\+\d{2} \(?\d{2}\)? \d{4,5}[- ]?\d{4,5}'
match = re.search(pattern, text)
print(match)

# buscando data
pattern = r'(\d{2})\/(\d{2})\/(\d{4})'
match = re.search(pattern, text)
print(match)
print('match completo (todos os grupos)', match.group(0))
print('match primeiro grupo (dia)', match.group(1))
print('match segundo grupo (mês)', match.group(2))
print('match terceiro grupo (ano)', match.group(3))

# buscando email (contato@ancieladvogados.com.br)
pattern = r'([a-zA-z]\w+)@([a-zA-z]\w+\.[a-zA-z\.]+)'
match = re.search(pattern, text)
print(match)
print('match completo (todos os grupos)', match.group(0))
print('match primeiro grupo (username)', match.group(1))
print('match segundo grupo (dominio)', match.group(2))

"""
UTILIZANDO MATCH
(retorna apenas o match)
(só casa com o começo do texto)
"""

# buscando por padrões em uma lista
lista = ['1teste', '4qualquer', 'maisuma5', 'teste6']

pattern = r'^\d' # buscando palavra que comece com um número decimal
pattern2 = r'.+\d$'  #buscando qualquer palavra que termine com um decimal

for i in lista:
    if re.match(pattern, i): print('START:', i)
    if re.match(pattern2, i): print('  END:', i)

"""
TRABALHANDO COM MULTILINHAS
(tem que ser com o search, só vai funcionar com o match se for algo no começo da primeira linha)
"""
# pattern = r'(?m)^' o m é um metacaracter "moderno" que permite sinalizar multilinhas
pattern = r'^\w+@\w+\.[a-zA-z\.]+'
match = re.search(pattern, text, re.MULTILINE) # re,MULTILINE é uma flag que simboliza o (m)
print(match)

"""
UTILIZANDO re.compile
retorna um array com os matches
(mais performático, trabalha com o findall - similar ao /g)
"""
pattern = re.compile(r'(\d{2}):(\d{2})') # se dividir por grupo para cada match retorna uma tupla
match = pattern.findall(text)
print(match)

"""
MANIPULANDO ARQUIVOS COM EXPRESSÕES REGULARES
(html)
"""
path = '/home/yreis/sb/socialbase-frontend/app/index.html'
with open(path) as f:
    html = f.read()
    pattern = re.compile(r'(https?\/\/|www)\.([\w?]+)\.?([\w?]+)')
    match = pattern.findall(html)
    print(match)

"""
UTILIZANDO O MÉTODO SUB
(com retrovisor)
"""
# substituindo a data para um padrão americano
match = re.sub(r'(\d{2})\/(\d{2})\/(\d{4})', r'\g<2>-\g<1>-\g<3>', text) # \g em python para selecionar retrovisores numéricos
print(match)

"""
UTILIZANDO O MÉTODO SPLIT
"""
# fazendo o split por linhas
match = re.split(r'\n', text) # também é possível passar um último parâmetro para o máximo de divisões. O último resultado vai pegar todo o restante do resultado
print(match)

"""
FLAGS
(re.M = multiline | re.I = ignore case | re.DOTALL = casa todas as sentenças encontradas)
"""
pattern = re.compile(r'^[a-z].+$', re.M|re.I)
match = pattern.findall(text)
print(match)
