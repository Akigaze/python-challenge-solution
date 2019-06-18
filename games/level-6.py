import os
import pickle
import re
from os import path
from zipfile import ZipFile

import requests

page_url = "http://www.pythonchallenge.com/pc/def/channel.html"

number_regex = re.compile(r'(?<=\s)(\d+)[\b]?')
zip_file_path = "..//files//channel.zip"

zip_obj = ZipFile(zip_file_path, "r")
file_names = zip_obj.namelist()
next_file = "readme"

comments = []

while True:
    content = zip_obj.read(next_file + ".txt").decode()
    matcher = number_regex.search(content)
    comment = zip_obj.getinfo(next_file + ".txt").comment.decode()
    comments.append(comment)
    print(content)
    if matcher:
        next_file = matcher.group(1)
    else:
        break

print("".join(comments))

zip_obj.close()
