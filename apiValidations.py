import json

import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php", params={'AuthorName':'Rahul Shetty2'},)
print(type(response.text))
print(response.text)
# json.loads() method parses json data and returns Dictionary
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])
# but, the json data is in List.
print(type(dict_response))
# .json() method is automatically recognizes the data type of the data, returns accordingly either List or Dictionary
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with ISBN RGHCC
for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break

expectedBook = {
    'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'
}
assert actualBook == expectedBook
