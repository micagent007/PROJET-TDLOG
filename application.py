import model
import random as rd
import beer_load

init_price={}
for i in range(len(beer_load.beer_list)):
    init_price[beer_load.beer_list[i].get_name()]=beer_load.beer_list[i].get_price()

            
        



#-------------------------------------------------------------------------------------------------------

def fonction_de_conso(beers, tab, init_p):
    consos={}
    for beer in beers :
        consos[beer.get_name()]=int(rd.randint(0,100)/tab.prices[beer.get_name()][tab.iter]*init_p[beer.get_name()]+0.5)
    return consos

#début changement pour ctrl z



#-------------------------------------------------------------------------------------------------------
'''
alphabet="abcdefghijklmnopqrstuvwxyz"
tab=model.price_table()
beers=[]

for k in range(5):
    size_name=rd.randint(1,7)
    name=""
    for i in range(size_name):
        name+=alphabet[rd.randint(0,25)]
    beer_i=model.beer(name,name,rd.randint(1,13),name)
    beers.append(beer_i)
    tab.add_beer(beer_i)

for k in range(300):
    

    
    consos=fonction_de_conso(beers, tab)
    tab.adjst_conso(consos)
    fonction_model_1(tab,beers)
    if k == 180:
        size_name=rd.randint(1,7)
        name=""
        for i in range(size_name):
            name+=alphabet[rd.randint(0,25)]
        beer_i=model.beer(name,name,rd.randint(1,13),name)
        beers.append(beer_i)
        tab.add_beer(beer_i)

beer_all=model.beer("all","all",0,"all")
tab.draw_curve(beer_all)
for beer in beers:
    tab.draw_curve(beer)'''

for k in range(300):

    consos=fonction_de_conso(beer_load.beer_list,beer_load.tab,init_price)
    beer_load.tab.adjst_conso(consos)
    beer_load.tab.model_function()

beer_all=model.beer("all","all",0,"all")
beer_load.tab.draw_curve(beer_all)
for beer in beer_load.beer_list:
    beer_load.tab.draw_curve(beer)












