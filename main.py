import requests


api_key = "321ab006b85541148c96fe568e858067"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-03"
       "&sortBy=publishedAt&apiKey=321ab006b85541148c96fe568e858067")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Print title and description of article
for article in (content["articles"]):
    print(article["title"])
    print(article["description"])