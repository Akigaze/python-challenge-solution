import re
from collections import namedtuple

import requests

page_url = "http://www.pythonchallenge.com/pc/def/equality.html"

url = "http://www.pythonchallenge.com/pc/def/equality.html"
response = requests.get(url)
# print(response.text)

matcher = re.search(r'(?<=<!--\n)([a-zA-Z\n]+)(?=\n-->)', response.text)
target_text = matcher.group(1)
print(target_text)

matchers = re.findall(r'(?<=[a-z\n])([A-Z]{3})([a-z])([A-Z]{3})(?=[a-z\n])', target_text, flags=re.MULTILINE)
print(matchers)

solution = "".join([m[1] for m in matchers])
print("solution is : ", solution)

