from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        diction = {
            "rur" : {
                "rur": 1,
                "usd": 0.0124,
                "eur": 0.0109
            },
            "usd" : {
                "rur": 80.9644,
                "usd": 1,
                "eur": 0.8808
            },
            "eur" : {
                "rur": 91.9169,
                "usd": 1.1353,
                "eur": 1
            }
        }

        _from = str(request.form.get('from'))
        _to = str(request.form.get('to'))
        try:
            _convertable = float(request.form.get('convertable'))
        except:
            return render_template('index.html', ans="Ошибка")
        else:
            conv = _convertable
            _convertable *= diction[_from][_to]

    return render_template('index.html', conv=conv, ans=_convertable)

if __name__ == '__main__':
    app.run()
