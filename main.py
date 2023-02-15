from flask import Flask, send_file, render_template, request
import jinja2

import application
from model import beer
from beer_load import *
from application import *
from recommandation import *
import time

app = Flask(__name__, static_folder='static')
app.debug = True

n = 120

conso = fonction_de_conso(beer_load.beer_list, beer_load.tab, application.init_price)
beer_load.tab.adjst_conso(conso)
beer_load.tab.model_function()
for selected_plot in beer_list:
    tab.draw_curve(selected_plot.get_name())
tab.draw_curve('all')

@app.route('/courbes', methods=['GET', 'POST'])
def courbes():
    selected_plot = 'all'
    if request.method == 'POST':
        selected_plot = request.form['selected_plot']
    return render_template('courbes.html', beers=beer_load.beer_list, selected_plot=selected_plot)

@app.route('/countdown-finished')
def countdown_finished():
    beer_load.tab.adjst_conso(conso)
    beer_load.tab.model_function()
    for selected_plot in beer_list:
        tab.draw_curve(selected_plot.get_name())
    tab.draw_curve('all')
    return

@app.route('/accueil')
def index():
    return render_template('accueil.html', time_left=n)


@app.route('/recommandation')
def recommandation_display():
    beer = beer_load.beer_list[recommandation(309) % tab.nb_beers]
    return render_template('recommandation.html', beers=beer, time_left=n)


@app.route('/tableau', methods=['GET', 'POST'])
def table_of_price():
    if request.method == 'POST':
        selected_plot = request.form['selected_plot']
        conso[selected_plot] += 1
    return render_template('tableau.html', beers=beer_load.beer_list, time_left=n)


if __name__ == '__main__':
    app.run()
