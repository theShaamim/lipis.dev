# coding: utf-8

import flask

import config

from main import app


@app.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt(challenge):
  responses = {
      'FU51VSlX4gypQpOqmnq-E_F80VTjVX2YfVgLU3VrX3I': 'FU51VSlX4gypQpOqmnq-E_F80VTjVX2YfVgLU3VrX3I.ypeY55PiET8BkyzWzASvUN5l52P2Tqi38of5mRR2rc8'
    }
  response = flask.make_response(responses.get(challenge, ''))
  response.headers['Content-Type'] = 'text/plain'
  return response
