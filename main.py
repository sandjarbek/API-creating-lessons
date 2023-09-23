import requests

# r= requests.get("https://newsapi.org/v2/everything?q=apple&from=2023-09-22&to=2023-09-22&sortBy=popularity&apiKey=c370e785b9f342068fe0038dfb7f400b")
# content = r.json()
# print(type(content))
#
# articles=content["articles"]
#
# for article in articles:
#     print("Title\n", article["title"], "\nDescription\n", article['description'])



def get_news(topic, from_date, to_date, api_key="c370e785b9f342068fe0038dfb7f400b"):
    url=f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}"
    r=requests.get(url)
    content=r.json()
    articles = content["articles"]
    results=[]
    for article in articles:
        results.append(f"Title\n, {article['title']}, '\nDescription\n', {article['description']}")
    return results

print(get_news(topic='apple', from_date="2023-9-22", to_date="2023-9-22"))