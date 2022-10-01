import requests 

data_pet = {
    
  "id": 1,
  "category": {
    "id": 1,
    "name": "string"
  },
  "name": "Mercy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 1,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post('https://petstore.swagger.io/v2/pet', json = data_pet)
print(response.text)


data_pet_name = {
    
  "id": 1,
  "category": {
    "id": 1,
    "name": "string"
  },
  "name": "Lucio",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put('https://petstore.swagger.io/v2/pet', json = data_pet_name)
print(response.text)

response = requests.get('https://petstore.swagger.io/v2/pet/1')
print(response.text)
