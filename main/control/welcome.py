# coding: utf-8

import flask

import config

from main import app


###############################################################################
# Welcome
###############################################################################
@app.route('/')
def welcome():
  return flask.render_template(
    'welcome.html',
    html_class='welcome',
  )


@app.route('/googlefe164a33bda4034b.html')
def google_verify():
  return 'google-site-verification: googlefe164a33bda4034b.html'


@app.route('/projects/')
def projects():
  return flask.render_template(
      'projects.html',
      html_class='projects',
      title='My Projects',
    )


@app.route('/gae-<talk>/')
def gae(talk):
  if talk not in ['aarhus', 'berlin', 'talk', 'lviv']:
    flask.abort(404)

  return flask.render_template(
      'gae-%s.html' % talk,
      html_class='gae-talk',
      title='Building Web Apps Like a Pro Using Google App Engine',
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
