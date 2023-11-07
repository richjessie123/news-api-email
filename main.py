import requests
from send_email import send_email

api_key = "321ab006b85541148c96fe568e858067"
topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=321ab006b85541148c96fe568e858067&"
       "language=en")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Print title and description of article and store in body variable
for article in (content["articles"][:20]):
    if article["title"] is not None:
        body = ("Subject: Today's News"
                + "\n" + body + article["title"]
                + "\n" + article["description"]
                + "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")

#Send email
send_email(message=body)

