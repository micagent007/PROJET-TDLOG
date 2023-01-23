import json
import model
import time


with open('biere_liste.json') as b_l:
    data = json.load(b_l)
    bieres={i: data[i] for i in range(len(data))}
#    print(bieres)

beer_list=[]
for i in range(len(data)):
    beer_list.append(model.beer(bieres[i]['name'],bieres[i]['img'],
         bieres[i]['price'],bieres[i]['description']))
for i in range(len(data)):
    print(beer_list[i].get_name(),beer_list[i].get_price())

tab=model.price_table()
tab.add_beers(beer_list)
