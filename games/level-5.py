import pickle
import requests

page_url = "http://www.pythonchallenge.com/pc/def/peak.html"

tip = "peakhell"

resource_url = "http://www.pythonchallenge.com/pc/def/banner.p"

response = requests.get(resource_url)
banner_content = pickle.loads(response.content)
print(banner_content)

for items in banner_content:
    print(items)
    print(sum([t[1] for t in items]))


count_list = [sum([t[1] for t in items]) for items in banner_content]
unique_count = list(set(count_list))[0]
print(unique_count)

result = []
for tuple_list in banner_content:
    line = ""
    for t in tuple_list:
        char = t[0]
        length = t[1]
        t_str = "".join([char for i in range(length)])
        line += t_str
    result.append(line)

print("\n".join(result))
