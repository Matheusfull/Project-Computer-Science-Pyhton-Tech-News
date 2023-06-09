from parsel import Selector
import requests
import time
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().replace("\xa0", "")
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.n::text").get()
    reading_time = int(selector.css("li.meta-reading-time::text").get()[0:2])
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".category-style .label::text").get()
    # print(summary)
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }


""" html = fetch("https://blog.betrybe.com/")
scrape_news(html) """
# reading_time = int(selector.css("li.meta-reading-time::text").
# re_first(r"\d{2}"))- Requisito bem chatinho


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    # 1 - Eu pego a primeira página de notícias e trago o html dela
    # 2 - faço um for em cada notícia para trazer as informações e adicioná-las
    # a um array e a cada for aumenta um contador para que eu possa
    # saber em qual número
    # está o contador para ter um limite, cujo este vem por parâmetro.
    # 3 - Se o limite de notícias não tiver na primeira página, então vamos
    # para a segunda. E assim até chegar ao limite de news ou não
    # ter mais página
    # 4 - Na página seguinte repete o processo 2
    # 5 - Coloca esse array no banco de dados
    # 6 - retorna o array

    url = "https://blog.betrybe.com/"
    list_news = []
    number_news = 0
    while number_news <= amount:  # 4
        response = fetch(url)  # 1
        selector_links = scrape_updates(response)
        for response_news in selector_links:  # 2
            html_news = fetch(response_news)
            data_news = scrape_news(html_news)
            list_news.append(data_news)
            number_news += 1
            if number_news == amount:
                break
        url = scrape_next_page_link(response)
        if url is None or number_news == amount:  # 3
            break
        # next_page = url babaquice do caraca, sem else
    create_news(list_news)  # 5
    return list_news  # 6

# print(get_tech_news(20))
