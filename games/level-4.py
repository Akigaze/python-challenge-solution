import re
from collections import namedtuple

import requests

page_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
start_nothing = 12345
# start_nothing = 52899
next_nothing = 0
response = requests.get(base_url % start_nothing)

while True:
    tip = response.text
    matcher = re.search(r'(?<=\s)(\d+)$', tip)
    if matcher:
        next_nothing = int(matcher.group(1))
        response = requests.get(base_url % next_nothing)
    elif "Divide" in tip:
        next_nothing /= 2
        response = requests.get(base_url % next_nothing)
    else:
        print(tip)  # peak.html
        break
    print(tip, next_nothing)


