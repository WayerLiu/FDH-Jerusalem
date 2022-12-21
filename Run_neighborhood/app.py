from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import Neighbor
from exts import db
import pandas as pd

app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)


def get_map():
    df = pd.read_csv('total_list_permatch_3.0.csv')
    df = df[~df['latitudes_g'].isnull()]
    return df.to_json(orient='records')
    # return df

@app.route('/')
def index():
    context = {
        'neighbors': Neighbor.query.all()
    }
    coord = get_map()
    return render_template('index.html', **context, coord=coord)


@app.route('/neighbor_list')
def neighbor_list():
    context = {
        'neighbors': Neighbor.query.all()
    }
    return render_template('neighbor_list.html', **context)


@app.route('/search/', methods=['GET','POST'])
def search():
    keyword = request.form.get('keyword')
    context = {
        'neighbors': Neighbor.query.filter(Neighbor.Neighborhood.like("%"+keyword+"%")).all()

    }
    return render_template('search.html', key=keyword, **context)

# @app.route('/details/', methods=['GET','POST'])
# def search():
#     keyword = request.form.get('keyword')
#     context = {
#         'neighbors': Neighbor.query.filter(Neighbor.Neighborhood.like("%"+keyword+"%")).all()
#
#     }
#     return render_template('search.html', key=keyword, **context)

@app.route('/Inhabitants')
def Inhabitants():
    context = {
        'neighbors': Neighbor.query.all()
    }
    coord = get_map()
    return render_template('Inhabitants.html', **context, coord=coord)

@app.route('/Initiative')
def Initiative():
    context = {
        'neighbors': Neighbor.query.all()
    }
    coord = get_map()
    return render_template('Initiative.html', **context, coord=coord)


@app.route('/details/<index>/')
def details(index):
    # index = session['index']
    record = Neighbor.query.filter(Neighbor.index == index).first()
    return render_template('details.html', neighborhood=record)


if __name__ == '__main__':
    app.run()
