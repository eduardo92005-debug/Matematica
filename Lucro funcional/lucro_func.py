import random
import time

random.seed(time.time())
def productFunction(price=0.0):
    return {
        "price" : price,
        "demands" : 0,
        "infinitesimal increment": 0.0,
        "quality":0
    }

def workFunction(collection_products, cost_price, max_profit_price):
    for product in collection_products:
        product["quality"] = random.randint(0,10)
        product["price"] = random.randrange(cost_price,max_profit_price)
    return 1
def consumerFunction(collection_products, variability=0):
    index_choice = random.randint(0,variability-1)
    product_chosen = collection_products[index_choice]
    product_chosen["demands"] += 1
    product_chosen["infinitesimal increment"] += 0.5
    inf_inc = product_chosen["infinitesimal increment"]
    product_chosen["price"] += inf_inc/100000
    
coll_products = [productFunction(), productFunction(), productFunction(),productFunction(),productFunction(),productFunction(),productFunction(),productFunction(),productFunction(),productFunction()]   

workFunction(coll_products,15,20)
variability = len(coll_products)
for i in range(10000):
    print('Iteração número: %d' %i)
    consumerFunction(coll_products, variability)
    print(coll_products[0])
    print(coll_products[1])
    print(coll_products[2])
    print(coll_products[3])
    print(coll_products[4])
    print(coll_products[5])
    print(coll_products[6])
    print(coll_products[7])
    print(coll_products[8])
    print(coll_products[9])
