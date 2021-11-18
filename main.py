import re
import requests

def is_url_from_wiki(link):

  test_string = link

  matched = re.match("^https?\:\/\/([\w\.]+)wikipedia.org\/\w+\/\w+", link)
  is_match = bool(matched)

  return is_match

def get_table_of_contents(link):

  codigo_fonte = requests.get(link).text

  topicos = re.findall(r'<span.*class=.toctext.*[\w]+.*?<\/span>', codigo_fonte)

  for i in topicos: print(i.split('<span class="toctext">')[1].split('</span>')[0] + '\n')

def get_wiki_references(link):

  codigo_fonte = requests.get(link).text

  wiki_refs = re.findall(r'a href="\/wiki([^"]*).', codigo_fonte)

  for i in wiki_refs: print(i + '\n')

def get_article_images(link):

  codigo_fonte = requests.get(link).text

  images = re.findall(r'\<img.+src\=(?:\"|\')(.+?)(?:\"|\')(?:.+?)\>', codigo_fonte)

  for i in images: print(i + '\n')

def menu_principal():

  url = input('Vamos analisar qual link da Wikipédia? \n')

  if not is_url_from_wiki(url):
    print('Esse link não é da Wikipédia. \nAssim tu me quebra as pernas.. :( Roda o código de novo.')

  else:
    print('\nMuito bem! Você digitou um link válido da Wikipédia. O que faremos? \n')
    escolha = input('Escolha a análise: \n\n 1- Ler Table of Contents \n 2- Ler artigos do Wikipedia referenciados \n 3- Ler nomes dos arquivos de imagem \n \n')

    print('\nProcessando ;) \n')

    if escolha == '1':
      get_table_of_contents(url)

    elif escolha == '2':
      get_wiki_references(url)

    elif escolha == '3':
      get_article_images(url)

    else:
      print('Escolha uma das alternativas corretas.')
      print('Rode o código novamente.')


menu_principal()
