#!python
from flask import Flask, request

app = Flask(__name__)

@app.route('/echo')
def echo():
    return 'you said: {}'.format(request.args.get('text',''))

if __name__ == '__main__':
    app.run()
