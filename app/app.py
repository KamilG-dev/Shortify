import random
import string
from flask import Flask, render_template, request

from database.models import Url
from database.database import SessionLocal
app = Flask(__name__)

app.session = SessionLocal()

def generate_unique_shorten_url() -> str:
    done = False
    while not done:
        shorten = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        url = app.session.query(Url).filter_by(short_url=shorten).first()

        if url is None:
            done = True
    
    return shorten


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten')
def shorten():
    url = request.args.get('url')
    if not url:
        return render_template('index.html', error='Please enter a URL')
    else:
        url_object = app.session.query(Url).filter_by(long_url=url).first()
        if url_object is not None:
            return render_template('index.html', info='This url was already shortened', url=url_object)
        shortened_url = generate_unique_shorten_url()
        url_object = Url(short_url=shortened_url, long_url=url)
        
        app.session.add(url_object)
        app.session.commit()
        app.session.refresh(url_object)

        return render_template('index.html', info='Url shortened successfully', url=url_object)

@app.route('/<string:shortened_url>')
def link(shortened_url):
    print(shortened_url)
    url = app.session.query(Url).filter_by(short_url=shortened_url).first()
    if url is not None:
        return render_template('link.html', url=url)
    
    return render_template('index.html', error='Could not find that URL')

if __name__ == '__main__':
    app.run(debug=True)