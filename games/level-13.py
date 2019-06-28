from xmlrpc import client

LEVEL = 13
page_url = "http://www.pythonchallenge.com/pc/return/disproportional.html"
phone_book_url = "http://www.pythonchallenge.com/pc/phonebook.php"
hint_1 = "evil"
hint_of_lv12 = "Bert"

proxy = client.ServerProxy(phone_book_url)
print(proxy.phone(hint_1))
print(proxy.phone(hint_of_lv12))
