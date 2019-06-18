import re
import requests
from collections import namedtuple

page_url = "http://www.pythonchallenge.com/pc/def/ocr.html"

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
response = requests.get(url)
# print(response.text)

matcher = re.search(r'(?<=<!--\n)(%[\w\W]+)(?=\n-->)', response.text, flags=re.M)
target_text = matcher.group(1)
print(target_text)

char_counter = {}
for char in target_text:
    if char_counter.get(char) is None:
        char_counter[char] = 0
    char_counter[char] += 1

Char = namedtuple('Char', ['code', 'count'])
char_count_list = [Char(k, v) for k, v in char_counter.items()]
char_count_list = sorted(char_count_list, key = lambda item: item.count)
for char in char_count_list:
    print("%s: %d" % (char.code, char.count))

solution = "".join([char.code for char in char_count_list if char.count == 1])
print("solution is : ", solution)
