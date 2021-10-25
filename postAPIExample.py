import requests
from payload import *
from utilities.configurations import *
from utilities.resourses import *

url = getConfig()['API']['endpoint'] + ApiResourses.addbook
header = {'Content-Type': 'application/json'}
addbook_response = requests.post(url, json=addBookPayload("kgfc"), headers=header, )

json_response = addbook_response.json()

print(json_response)

bookID = json_response['ID']

# delete book
url = getConfig()['API']['endpoint'] + ApiResourses.deletebook
deletebook_response = requests.get(url, json={

    "ID": bookID

}, headers=header, )

json_response = deletebook_response.json()
print(json_response)
