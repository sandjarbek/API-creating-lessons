import requests



def get_news(country, api_key="c370e785b9f342068fe0038dfb7f400b"):
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r=requests.get(url)
    content=r.json()
    articles = content["articles"]
    results=[]
    for article in articles:
        results.append(f"Title\n, {article['title']}, '\nDescription\n', {article['description']}")
    return results

print(get_news(country='us'))
