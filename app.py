from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs





client_id='1002052005922-rr7bc2g3n2721gnb0a61242gog3mt84v.apps.googleusercontent.com'
client_secret='EzJ0lyZxhD_tkIAG5Y5PKbxO'
redirect_uri = 'https://oauth-iesgn.rhcloud.com/oauth2callback'
scope = ['https://www.googleapis.com/auth/youtube','https://www.googleapis.com/auth/userinfo.profile']
token_url = "https://accounts.google.com/o/oauth2/token"


@get('/google')
def get_token():
    return template('oauth2.tpl')


def token_valido():
  token=request.get_cookie("token", secret='some-secret-key')
  if token:
    token_ok = True
    try:
      oauth2 = OAuth2Session(client_id, token=token)
      r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    except TokenExpiredError as e:
      token_ok = False
  else:
    token_ok = False
  return token_ok

@get('/youtube')
def info_youtube():
  if token_valido():
    redirect("/perfil")
  else:
    response.set_cookie("token", '',max_age=0)
    oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
    authorization_url, state = oauth2.authorization_url('https://accounts.google.com/o/oauth2/auth')
    response.set_cookie("oauth_state", state)
    redirect(authorization_url)

@get('/oauth2callback')
def get_token():

  oauth2 = OAuth2Session(client_id, state=request.cookies.oauth_state,redirect_uri=redirect_uri)
  token = oauth2.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)
  response.set_cookie("token", token,secret='some-secret-key')
  redirect("/perfil")
  
@get('/perfil')
def info():
  if token_valido():
    token=request.get_cookie("token", secret='some-secret-key')
    oauth2 = OAuth2Session(client_id, token=token)
    r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    doc=json.loads(r.content)
    return '<p>%s</p><img src="%s"/><br/><a href="/logout">Cerrar</a>' % (doc["name"],doc["picture"])
  else:
    redirect('/youtube')

@get('/logout')
def salir():
  response.set_cookie("token", '',max_age=0)
  redirect('/youtube')

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')
