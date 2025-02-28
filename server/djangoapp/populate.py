from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "logo_url":"https://banner2.cleanpng.com/20180413/oyw/avfea0dju.webp"},
        {"name":"Mercedes", "description":"Great cars. German technology", "logo_url":"https://upload.wikimedia.org/wikipedia/commons/9/90/Mercedes-Logo.svg"},
        {"name":"Audi", "description":"Great cars. German technology", "logo_url":"https://pictures.dealer.com/k/keyesaudishermanoaksaoa/0416/d82ee5a1af7fd3baa30a98070b91144ax.jpg"},
        {"name":"Kia", "description":"Great cars. Korean technology", "logo_url":"https://cdn.freebiesupply.com/logos/large/2x/kia-logo-png-transparent.png"},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "logo_url":"https://e7.pngegg.com/pngimages/802/655/png-clipart-2016-toyota-4runner-car-toyota-c-hr-concept-logo-toyota-emblem-trademark.png"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], logo_url=data['logo_url']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":4231, "price":10000},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":3166, "price":10000},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":9013, "price":10000},
      {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":1290, "price":10000},
      {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":9271, "price":10000},
      {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":327, "price":10000},
      {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":256, "price":10000},
      {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":8791, "price":10000},
      {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":1552, "price":10000},
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id":9931, "price":10000},
      {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id":11182, "price":10000},
      {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id":218, "price":10000},
      {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id":8582, "price":10000},
      {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id":3123, "price":10000},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id":1114, "price":10000},
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'], dealer_id=data['dealer_id'], price=data['price'])