from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def label():
    return "<strong>Миссия Колонизация Марса</strong>"


@app.route('/index')
def devis():
    return "<strong>И на Марсе будут яблони цвести!</strong>"


@app.route('/promotion')
def promotion():
    return """<strong><p>Человечество вырастает из детства.</p>
                      <p>Человечеству мала одна планета.</p>
                      <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                      <p>И начнем с Марса!</p>
                      <p>Присоединяйся!</p>
              </strong>"""


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://e7.pngegg.com/pngimages/1000/382/png-clipart-blood-moon-earth-mars-planet-solar-system-terraforming-jupiter-atmosphere-sphere.png" style="height: 700px;">
                  </body>
                </html>'''


@app.route("/promotion_image")
def promotion_image():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')