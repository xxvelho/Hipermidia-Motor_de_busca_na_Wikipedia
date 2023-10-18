import xml.dom.minidom as m
from collections import defaultdict

doc = m.parse('verbetesWikipedia.xml')
page_list = doc.getElementsByTagName('page')

# Tarefa 05 e 06 Usando um grafo como Hash invertida para armazenar os <id>, <title>,
# palavras simples e palavras compostas. Guardando as ocorrências em dicionários
class GraphNode:
  def __init__(self, id, title):
    self.id = id
    self.title = title
    self.word_occurrences = defaultdict(int)  # Dicionário para armazenar as ocorrências de palavras simples
    self.phrase_occurrences = defaultdict(int)  # Dicionário para armazenar as ocorrências de palavras compostas

class Graph:
  def __init__(self):
    self.nodes = {}  # Dicionário para armazenar os nós do grafo

# Grafo para armazenar as páginas e suas ocorrências de palavras
graph = Graph()

for page in page_list:
  page_id = page.getElementsByTagName('id')[0].firstChild.nodeValue
  title_name = page.getElementsByTagName('title')[0].firstChild.nodeValue

  # Criando um nó do grafo para a página
  page_node = GraphNode(page_id, title_name)

  title_element = page.getElementsByTagName('title')[0]
  title_text = title_element.firstChild.wholeText.strip()
  title_words = title_text.split()

  # Adiciona palavras do titulo em word_occurrences e phrases_occurrences
  for i in range(0, len(title_words) - 1, 2):
    word1 = title_words[i].strip('.,?!()[]{}').lower()
    word2 = title_words[i + 1].strip('.,?!()[]{}').lower()
    if len(word1) >= 4 and len(word2) >= 4:  # Ignora palavras com menos de 4 caracteres
      phrase = "{} {}".format(word1, word2)
      page_node.phrase_occurrences[phrase] += 10
    if len(word1) >= 4:
      page_node.word_occurrences[word1] += 10
    if len(word2) >= 4:
      page_node.word_occurrences[word2] += 10


  text_element = page.getElementsByTagName('text')[0]
  text = text_element.firstChild.nodeValue
  words = text.split()  # Divide o texto em palavras

  #  Adiciona palavras do titulo em word_occurrences e phrases_occurrences
  for i in range(0, len(words) - 1, 2):
    word1 = words[i].strip('.,?!()[]{}').lower()
    word2 = words[i + 1].strip('.,?!()[]{}').lower()
    if len(word1) >= 4 and len(word2) >= 4:  # Ignora palavras com menos de 4 caracteres
      phrase = "{} {}".format(word1, word2)
      page_node.phrase_occurrences[phrase] += 1
    if len(word1) >= 4:
      page_node.word_occurrences[word1] += 1
    if len(word2) >= 4:
      page_node.word_occurrences[word2] += 1


  # Adiciona o nó da página ao grafo
  graph.nodes[page_node.id] = page_node

def busca():
  # Palavra a ser pesquisada
  search_string = input("Digite a string de busca: ")
  # Guarda o tamanho da string para saber se a busca é simples ou composta
  qtd_words = len(search_string.split())
  
  # Pesquisa a palavra no grafo
  result_pages = []
  total_occurrences = 0
  for node_id, node in graph.nodes.items():
    # Busca simples
    if qtd_words == 1:
      if search_string.lower() in node.word_occurrences:
        occurrences = node.word_occurrences[search_string.lower()]
        total_occurrences += occurrences
        result_pages.append((node, node.word_occurrences[search_string.lower()]))
    
    # Busca composta
    elif qtd_words == 2:
      if search_string.lower() in node.phrase_occurrences:
        occurrences = node.phrase_occurrences[search_string.lower()]
        total_occurrences += occurrences
        result_pages.append((node, node.phrase_occurrences[search_string.lower()]))
  
  # Ordena as páginas por número de ocorrências em ordem decrescente
  sorted_result_pages = sorted(result_pages, key=lambda x: x[1], reverse=True)
  
  # Imprime a soma de todas as ocorrências das páginas encontradas
  print("\nTotal de ocorrências da palavra '{}': {}\n".format(search_string, total_occurrences))
  
  # Imprime as páginas e o número de ocorrências da palavra
  for page, occurrences in sorted_result_pages[:20]:
    print("{}\t=>\t{}, Ocorrências: {}".format(page.id, page.title, occurrences))

# realizando 10 buscas
for _ in range(10):
  busca()

# Tarefa 01 - Calcula o número de tags <page>
'''
num_pages = len(page_list)
print("Número de tags <page>: {}".format(num_pages))
'''

# Tarefa 02 - Imprimir o <id> e <title> de cada uma das <page> do arquivo
'''
for page in page_list:
  # Obtém o valor da tag <id>
  id_element = page.getElementsByTagName('id')[0]
  page_id = id_element.firstChild.nodeValue

  # Obtém o valor da tag <title>
  title_element = page.getElementsByTagName('title')[0]
  title_text = title_element.firstChild.nodeValue

  # Imprime o <id> e <title> de cada <page>
  print("ID: {}, Título: {}".format(page_id, title_text))
'''

# Tarefa 03 - O usuário informa uma string de busca. Você deve listar apenas os <id> 
# e <title> daquelas páginas em que aparece aquela string de busca no <title>.
'''
search_string = input("Digite a string de busca: ")

# Itera sobre cada tag <page> e verifica se a string de busca está no <title>
for page in page_list:
  # Obtém o valor da tag <title>
  title_element = page.getElementsByTagName('title')[0]
  title_text = title_element.firstChild.nodeValue

  # Verifica se a string de busca está no <title> (ignorando maiúsculas/minúsculas)
  if search_string.lower() in title_text.lower():
    # Obtém o valor da tag <id>
    id_element = page.getElementsByTagName('id')[0]
    page_id = id_element.firstChild.nodeValue

    # Imprime o <id> e <title> das páginas que correspondem à busca
    print("ID: {}, Título: {}".format(page_id, title_text))
'''

# Tarefa 04 - Mostrar o resultado de busca de acordo com a contagem de ocorrências. 
# As páginas com mais ocorrências devem aparecer na frente das demais.
# Aquelas com ocorrência no title contam como 10, no text contam como 1.
'''
search_string = input("Digite a string de busca: ")

# Dicionário para armazenar as ocorrências de páginas
word_occurrences = defaultdict(int)

# Itera sobre cada tag <page> e verifica se a string de busca está no <title> ou no <text>
for page in page_list:
  page_id = page.getElementsByTagName('id')[0].firstChild.nodeValue
  title_name = page.getElementsByTagName('title')[0].firstChild.nodeValue
  chave = page_id + "\t=>\t" + title_name

  title_element = page.getElementsByTagName('title')[0]
  title_text = title_element.firstChild.wholeText.strip()
  title_words = title_text.split()

  # Adiciona palavras do titulo em word_occurrences
  for i in range(len(title_words) - 1):
    word = title_words[i].strip('.,?!()[]{}')
    if word.lower() == search_string.lower():
      word_occurrences[chave] += 10

  text_element = page.getElementsByTagName('text')[0]
  text = text_element.firstChild.nodeValue
  words = text.split()

  # Adiciona palavras do texto em word_occurrences
  for i in range(len(words) - 1):
    word = words[i].strip('.,?!()[]{}')
    if word.lower() == search_string.lower():
      word_occurrences[chave] += 1


# Ordena as páginas com base nas ocorrências em ordem decrescente
sorted_pages = sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True)

total_word_occurrences = sum(word_occurrences.values())
print("\nTotal de ocorrências da palavra '{}': {}\n".format(search_string, total_word_occurrences))

# Imprime as primeiras 20 páginas com maiores ocorrências
for chave, occurrences in sorted_pages[:20]:
    print("{}, Ocorrências: {}".format(chave, occurrences))
'''