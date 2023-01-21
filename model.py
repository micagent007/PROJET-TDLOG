import matplotlib.pyplot as plt
import random as rd
import mpld3


#-------------------------------------------------------------------------------------------------------

class beer:
    def __init__(self,name,path_image,price,description):
        self.name=name
        self.img=path_image
        self.price=price
        self.descr=description
        
    def change_price(self,new_price):
        self.price=new_price
        
    def get_name(self):
        return self.name
    
    def get_image(self):
        return self.img
    
    def get_price(self):
        return self.price
    
    def get_descr(self):
        return self.descr

#-------------------------------------------------------------------------------------------------------

colors=['red','green','blue','c','m','yellow','black','orange']



class price_table:
    
    def __init__(self):
        self.prices={}

        self.beers=[] #dictionnaire relaint une biere a sa ligne de prix
        self.beers_colors={} #couleur des bieres sur les courbes
        self.lim=0 #affichage
        self.conso={} #achats
        self.iter = 0 #à quelle itération de l update des prix est on ?
        self.nb_beers = 0
        self.alpha=0.2 #coef de prise en compte
        
    def add_beer(self,beer):
        if not beer in self.beers: #on ne rajoute pas une biere deja presente
            
            self.beers.append(beer)
            self.beers_colors[beer.get_name()]=colors[self.nb_beers]
            self.nb_beers+=1

            self.conso[beer.get_name()]=[0,0] #[0]conso totale, [1] actuelle
            
            if self.nb_beers == 1: #on regarde si la biere est ajoutee des le debut ou non
                self.prices[beer.get_name()]=[beer.get_price()]
                
            else:
                beer_prices=[None for k in range(self.iter)]
                        #None pour representer que la biere n'existait pas auparavant
                beer_prices.append(beer.get_price())
                self.prices[beer.get_name()]=beer_prices

                
            if beer.get_price()>self.lim :
                self.lim=beer.get_price() #affichage
        return

    def add_beers(self,beers):
        for i in range(len(beers)):
            self.add_beer(beers[i])
        return
    
    def adjst_prices(self):
        for beer in self.beers:
            self.prices[beer.get_name()].append(beer.get_price())
            #on suppose que la biere est deja rentree dans le tableau
            if beer.get_price()>self.lim :
                self.lim=beer.get_price() #affichage
        self.iter+=1
        return

    def adjst_conso(self,consos):
        for beer in self.beers:
            self.conso[beer.get_name()][0]+=consos[beer.get_name()]
            self.conso[beer.get_name()][1]=consos[beer.get_name()]


    

    
    def draw_curves_all(self):
        x=[i for i in range(self.iter+1)] #ligne de repere temporel
        for beer in self.beers:
            beer_departure=0
            while self.prices[beer.get_name()][beer_departure]==None:
                #on definie quand commencer la courbe
                beer_departure+=1
                
            plt.plot(x[beer_departure:],
                     self.prices[beer.get_name()][beer_departure:],
                     self.beers_colors[beer.get_name()],
                     label=beer.get_name())
            
        plt.ylim([0,self.lim +1])
        plt.legend()
        plt.show()
        #plt.savefig("all_beers")
        return
    
    #color='r' ou autre avc self.beer_colors a rajouter (faire en sorte qu elles aient ttes des couleurs diff
    # for e in dict e est la clef
    # plt.plot(x,y,color)

    def draw_curve(self,beer):
        if beer.get_name()=="all":
            self.draw_curves_all()
        else :
            x=[i for i in range(self.iter+1)] #ligne de repere temporel
            beer_departure=0
            while self.prices[beer.get_name()][beer_departure]==None:
                #on definie quand commencer la courbe
                beer_departure+=1
            plt.plot(x[beer_departure:],
                     self.prices[beer.get_name()][beer_departure:],
                     self.beers_colors[beer.get_name()])
            plt.ylim([0,self.lim +1])
            plt.xlabel(beer.get_name()+f"  {beer.get_price()} €")
            

            
            plt.show()
            #mpld3.show()
        #plt.savefig(beer.get_name())
        return

#-------------------------------------------------------------------------------------------------------

#model fonction

    def model_function(self):
        sum_conso_iter=0
        sum_conso_tot=0
        sum_prices=0

        for beer in self.beers:
            sum_conso_iter += self.conso[beer.get_name()][1]
            sum_conso_tot += self.conso[beer.get_name()][0]
            sum_prices += self.prices[beer.get_name()][self.iter]
        
        if sum_conso_iter == 0: #not div by 0
            return
        
        for beer in self.beers:
            new_price = self.alpha * self.conso[beer.get_name()][1] / sum_conso_iter
            new_price += (1 - self.alpha) * self.conso[beer.get_name()][0] / sum_conso_tot
            new_price *= sum_prices
            new_price = max(.5,new_price)
            new_price = min(5,new_price)
            new_price = int(new_price * 100 + .5)/100 #arrondi au centième
            beer.change_price(new_price)
        
        self.adjst_prices()
        return


#-------------------------------------------------------------------------------------------------------










        
