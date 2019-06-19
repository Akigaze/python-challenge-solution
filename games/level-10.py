import re
from collections import namedtuple

LEVEL = 10
page_url = "http://www.pythonchallenge.com/pc/return/bull.html"

# hint: a = [1, 11, 21, 1211, 111221,
hint = [1, 11, 21, 1211, 111221]
regex = re.compile(r"(\d)(\1*)")

for item in hint:
    piece = regex.findall(str(item))
    parts = [str(len(i + j)) + i for i, j in piece]
    print("".join(parts))

# 312211
# (3,)(1,)(2,2)(1,1)
# 13112221

# 13112221
# (1,)(3,)(1,1)(2,22)(1,)
# 1113213211
print("--------------------")

Item = namedtuple("Item", ("string", "length"))
first = Item("1", 1)
hint = [first]
cur = "1"
while len(hint) < 31:
    piece = regex.findall(str(cur))
    parts = [str(len(i + j)) + i for i, j in piece]
    cur = "".join(parts)
    hint.append(Item(cur, len(cur)))

print(hint[30].length)


