import math
from flask import Flask
app = Flask(__name__)


LYRICS = {'do': 'Doe, a deer a female deer',
         're': 'Ray, A drop of golden sun',
         'me': 'Me, a name I call myself',
         'fa': 'Far, a long long way to run',
         'so': 'Sew, a needle pulling thread',
         'la': 'La, a note to follow so',
         'ti': 'Tea, a drink with jam and bread'}

@app.route('/song/<name>')
def sound_of_music(name):
    res = LYRICS.get(name) if LYRICS.get(name) else f"The note {name} is not part of the song!"
    return f"<h1>{res}</h1>"

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=5000)