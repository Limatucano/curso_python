import functools

def mult(first, second):
    return first * second

result_normal = mult(2,4)

result_lambda = lambda first, second: first * second

#print(result_normal, result_lambda(2,4))


cart = [
    {
        "name": "book",
        "price": 50.5,
        "description": "first book about second war",
        "coupom" : None,
    },
    {
        "name": "book",
        "price": 50.5,
        "description": "first book about second war",
        "coupom" : None,
    },
    {
        "name": "book",
        "price": 50.5,
        "description": "first book about second war",
        "coupom" : None,
    },
    {
        "name": "plant b",
        "price": 30.5,
        "description": "its a beautiful plant, the scientific name is hepicilanys",
        "coupom" : "PLANTSTODAY"
    },
    {
        "name": "plant a",
        "price": 20.0,
        "description": "its a beautiful plant, the scientific name is paubrasilience",
        "coupom" : "PLANTSTODAY"
    },
]

filter_products_with_coupom = list(filter(lambda x: x.get("coupom") == "PLANTSTODAY",cart))

reduce_products_with_coupom = functools.reduce(lambda x,y: x + y, list(map(lambda x: x.get("price"), filter_products_with_coupom)))

print(reduce_products_with_coupom)