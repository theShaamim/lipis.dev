# coding: utf-8

import flask

import config

from main import app


###############################################################################
# Welcome
###############################################################################
@app.route('/')
@app.route('/<path:path>/')
def welcome(path=None):
  if path:
    return flask.redirect(flask.url_for('welcome'))
  return flask.render_template(
    'welcome.html',
    title='Panayiotis Lipiridis (Lipis)',
    html_class='welcome',
    description='Web dude at Wire',
  )


###############################################################################
# Sitemap stuff
###############################################################################
@app.route('/sitemap.xml')
def sitemap():
  response = flask.make_response(flask.render_template(
    'sitemap.xml',
    lastmod=config.CURRENT_VERSION_DATE.strftime('%Y-%m-%d'),
  ))
  response.headers['Content-Type'] = 'application/xml'
  return response


###############################################################################
# Warmup request
###############################################################################
@app.route('/_ah/warmup')
def warmup():
  # TODO: put your warmup code here
  return 'success'
