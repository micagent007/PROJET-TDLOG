import model
import random as rd
import beer_load

#-------------------------------------------------------------------------------------------------------


def fonction_model_1(tab,beers):
    sum_conso_iter=0
    sum_conso_tot=0
    sum_conso_beers={}

    sum_prices=0

    for beer in beers :
        sum_conso_iter += tab.conso[tab.beers[beer.get_name()]][tab.iter]
        sum_conso_beers[beer.get_name()] = 0

        sum_prices += tab.prices[tab.beers[beer.get_name()]][tab.iter]
        
        for k in range(tab.iter+1):
            c_beer_k = tab.conso[tab.beers[beer.get_name()]][k]
            if not c_beer_k == None :
                sum_conso_tot += c_beer_k
                sum_conso_beers[beer.get_name()] += c_beer_k



    for beer in beers :
        new_price = tab.alpha * tab.conso[tab.beers[beer.get_name()]][tab.iter] / sum_conso_iter
        new_price += (1 - tab.alpha) * sum_conso_beers[beer.get_name()] / sum_conso_tot
        new_price *= sum_prices
        
        new_price=max(0.5,new_price)
        new_price=min(5,new_price)
        
        beer.change_price(new_price)

    tab.adjst_prices(beers)
    
    return


def fonction_model_2(tab,beers):
    sum_conso=0


    
    for beer in beers :
        sum_conso+=tab.conso[tab.beers[beer.get_name()]][tab.iter]
    if tab.iter==1:
        for beer in beers :
            new_price=tab.conso[tab.beers[beer.get_name()]][tab.iter]*tab.nb_beers/sum_conso
            new_price=max(0.5,new_price)
            new_price=min(5,new_price)
            beer.change_price(new_price)
    else :
        for beer in beers :
            new_price=tab.conso[tab.beers[beer.get_name()]][tab.iter]*tab.nb_beers/sum_conso
            if not tab.prices[tab.beers[beer.get_name()]][tab.iter-1]==None:
                new_price+= tab.alpha*tab.prices[tab.beers[beer.get_name()]][tab.iter]
                new_price-= tab.alpha*tab.prices[tab.beers[beer.get_name()]][tab.iter-1]
            new_price=max(0.5,new_price)
            new_price=min(5,new_price)
            beer.change_price(new_price)
    tab.adjst_prices(beers)
    return
            
            
        



#-------------------------------------------------------------------------------------------------------

def fonction_de_conso(beers, tab):
    consos={}
    for beer in beers :
        consos[beer.get_name()]=rd.randint(0,100)/tab.prices[tab.beers[beer.get_name()]][tab.iter]
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

    consos=fonction_de_conso(beer_load.beer_list,beer_load.tab)
    beer_load.tab.adjst_conso(consos)
    fonction_model_1(beer_load.tab,beer_load.beer_list)

beer_all=model.beer("all","all",0,"all")
beer_load.tab.draw_curve(beer_all)
for beer in beer_load.beer_list:
    beer_load.tab.draw_curve(beer)












