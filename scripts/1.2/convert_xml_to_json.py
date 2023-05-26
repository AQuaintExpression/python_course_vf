import requests
from lxml import html

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
tree = html.fromstring(response.content)

# Extract the article title
title = tree.xpath('//*[@id="firstHeading"]/span/text()')[0]
print(title)

# Extract the list of references
references = tree.xpath('//*[@id="mw-content-text"]/div[1]/div[15]/ol/li')
results = []
print(len(references))
for reference in references:
    text = reference.xpath('//span[2]/cite/text()')
    results.append(text)

# Print the last 5 references
for reference in references[-5:]:
    print(reference.text_content())

