from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
import os
# from gevent.pywsgi import WSGIServer

if os.name != "nt":
    os.chdir(os.path.dirname(__file__))

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def blog():
    return render_template('math.html')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(".", "robots.txt")

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(".", "sitemap.xml")

if __name__ == "__main__":
    # http_server = WSGIServer(('0.0.0.0', 2012), app)
    # http_server.serve_forever()
    app.run(debug=True)