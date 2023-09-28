import requests



KEY = "367a1ef850b70165a524a7ee56e26d6f"
city_name = "Aleppo"
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={KEY}"

r = requests.get(url)

content = r.json()

print(content['list'][1]['dt_txt'])

print(content['list'][1]['weather'][0]['description'])

print(content['list'][1]['main']['temp'])

rows = content['list']

with open("data.txt", "a") as file:


    for row in rows:
        time = row['dt_txt']
        temperature = row['main']['temp']
        condition = row['weather'][0]['description']
        qator = f"{city_name},{time},{temperature},{condition}\n"
        file.write(qator)
