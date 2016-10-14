# coding: utf-8

import flask

from main import app


# Wedding related
@app.route('/polis')
def polis():
  return flask.redirect('https://goo.gl/maps/bEYkWr7aeGv')
