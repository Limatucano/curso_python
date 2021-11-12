
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

teste =     {
        "name": "plant a",
        "price": 30.0,
        "description": "its a beautiful plant, the scientific name is paubrasilience",
        "coupom" : "PLANTSTODAY"
    }

#dict_variable = {key:value for (key,value) in dictonary.items()}
a = {key:value * 2 if key == 'price' else value for key, value in teste.items() }



