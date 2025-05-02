import requests,pymongo
#Extract Data
products=requests.get('https://dummyjson.com/products').json()['products']
#print(type(products))  # <class 'list'>

#DB Connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db=client['11am']
product_col=db['products']
product_col.insert_many(products)
print("Product data writen success")