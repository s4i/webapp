from plot_graph import pg1,pg2,pg3,pg4
from flask import Flask, render_template, \
    request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

class SiteInfo:
    title = 'Data Visualization'


@app.route("/plot1/")
def plot_graph1():
    print(session.get('date', 'None'))
    #img_data = pg1(session.get('date', 'None'))
    img_data = pg2('sin')
    return img_data


@app.route("/plot2/<func>")
def plot_graph2(func='sin'):
    img_data = pg2(func)
    return img_data


@app.route("/plot3/")
def plot_graph3():
    img_data = pg3()
    return img_data


@app.route("/plot4/")
def plot_graph4():
    img_data = pg3()
    return img_data


@app.route("/get", methods=['GET'])
def get():
    session['date'] = request.args.getlist('date')
    date = session.get('date')
    date = ''.join(date)
    return render_template('index.html',
                            title=SiteInfo.title,
                            date=date)

@app.route('/')
def index():
    return render_template('index.html',
                           title=SiteInfo.title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
