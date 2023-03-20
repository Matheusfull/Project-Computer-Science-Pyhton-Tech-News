from tech_news.database import search_news
from datetime import datetime


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


# print(search_by_title("Algoritmo"))


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        # data_format = date.fromisoformat(date)
        correct_format = datetime.strptime(
            date, "%Y-%m-%d"
            ).strftime("%d/%m/%Y")
        a_data = search_news({"timestamp": correct_format})
        search_filter = [(el["title"], el["url"]) for el in a_data]
    except ValueError:
        raise ValueError("Data inválida")
    return search_filter


# data = "2023-03-14"
# data_format = date.fromisoformat(data)
# correct_format = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
# print(correct_format)
print(search_by_date("2023-03-14"))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    array_search_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
        )
    search_filter = [
        (el["title"], el["url"]) for el in array_search_category
    ]
    return search_filter


# print(search_by_category("Ferramentas"))
