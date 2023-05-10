# VARIABLES
name = "Jose"
age = 26
isAdmin = True

print(f"{name} has {str(age)} years and that is equal to {isAdmin}")

# COLLECTION

UserCollection = {
    "name": "Joseph",
    "age": 26,
    "genere": "Male"
}

print(UserCollection)

# FUNCTION
def sumar(num1, num2):
    if(not num1) or (not num2):
        return "Numbers are required!"
    else:
        return num1 + num2
    
result = sumar(5, 10)
print(result)

# REQUESTS
import requests

def getPost():
    url_jsonplaceholder = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url_jsonplaceholder)

    if response.status_code == 200:
        data = response.json()
        return data
    else: 
        return 'Error request'

print(getPost())