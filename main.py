from flask import Flask, send_file,render_template,request
from matplotlib import pyplot as plt

import application
import beer_load
from beer_load import *
from application import *
from recommandation import *

app = Flask(__name__,static_folder='static')
app.debug = True

@app.route('/courbes', methods=['GET', 'POST'])
def courbes():
    selected_plot = 'all'
    if request.method == 'POST':
        selected_plot = request.form['selected_plot']
        conso = fonction_de_conso(beer_load.beer_list, beer_load.tab, application.init_price)
        beer_load.tab.adjst_conso(conso)
        beer_load.tab.model_function()
        tab.draw_curve(selected_plot)
    return render_template('courbes.html', beers=beer_load.beer_list,selected_plot=selected_plot)

@app.route('/accueil')
def index():
    return render_template('accueil.html')

@app.route('/recommandation')
def recommandation_display():
    beer=beer_load.beer_list[recommandation(306)%tab.nb_beers]
    return render_template('recommandation.html', beers=beer)

@app.route('/tableau')
def table_of_price():
    return render_template('tableau.html', beers=beer_load.beer_list)



if __name__ == '__main__':
    app.run()