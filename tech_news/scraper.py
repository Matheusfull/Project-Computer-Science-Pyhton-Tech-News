from parsel import Selector
import requests
import time


#  Requisito 1
# A função deve receber uma URL
def fetch(url):
    try:
        # A função deve respeitar um Rate Limit de 1 requisição por segundo;
        # Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo
        # entre cada requisição que fizer.
        time.sleep(1)
        # A função deve fazer uma requisição HTTP get para esta URL
        # utilizando a função requests.get
        # Caso a requisição não receba resposta em até 3 segundos,
        # ela deve ser abandonada
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        # Caso a requisição seja bem sucedida com Status Code 200: OK,
        # deve ser retornado seu conteúdo de texto;
        if response.status_code == 200:
            # A função deve retornar o conteúdo HTML da resposta.
            return response.text
        # Caso a resposta tenha o código de status diferente de 200,
        # deve-se retornar None
        return None
    except requests.Timeout:
        return None


# print(fetch("https://blog.betrybe.com"))
# print("hello, word")


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    if selector:
        return selector.css("a.cs-overlay-link ::attr(href)").getall()
    return []


""" html = fetch("https://blog.betrybe.com/")
print(scrape_updates(html)) """


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(".next.page-numbers ::attr(href)").get()
    # o seletor next a.page-numbers ::attr(href) está errado porque
    # não precisa referenciar que é um link, só passar a classe
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
