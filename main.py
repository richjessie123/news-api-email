import requests
from send_email import send_email

api_key = "321ab006b85541148c96fe568e858067"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-03"
       "&sortBy=publishedAt&apiKey=321ab006b85541148c96fe568e858067")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Print title and description of article and store in body variable
for article in (content["articles"]):
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")

#Send email
send_email(message=body)

