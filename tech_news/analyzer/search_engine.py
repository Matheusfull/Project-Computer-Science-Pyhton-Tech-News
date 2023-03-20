from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    # fiquei que nem uma babaca tentando { "title": title }...
    array_search_title = search_news(
        {"title": {"$regex": title, "$options": "i"}}
        )
    search_filter = [
        (el["title"], el["url"]) for el in array_search_title
    ]
    return search_filter


print(search_by_title("Algoritmo"))


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
