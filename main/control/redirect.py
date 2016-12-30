# coding: utf-8

import flask

from main import app


# Wedding related
@app.route('/map')
@app.route('/polis')
@app.route('/map/')
def map():
  return flask.redirect('https://goo.gl/maps/bEYkWr7aeGv')


@app.route('/wed/')
@app.route('/weding/')
@app.route('/wedding/')
def wedding():
  return flask.redirect('https://wedding.lip.is')
