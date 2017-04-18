from sys import argv
import bottle

from bottle import Bottle,route,run,request,template,static_file
from lxml import etree
import requests

@route('/', method="get")
def intro():
	return template('template.tpl')



@route('/formulario',method="post")
def formulario():
	a=open("key","r")
	key=a.readline()
	ciudad = request.forms.get('ciudad')
	tipo = request.forms.get('tipo')
	payload={"app_key":key, "location": ciudad, "keywords":tipo}
	r=requests.get("http://api.eventful.com/rest/events/search",params=payload)
	#r=requests.get("http://api.eventful.com/rest/events/search?keywords="+tipo+"&location="+ciudad+"&app_key="+key)

	if r.status_code == 200:
		doc = etree.fromstring(r.text.encode ('utf-8'))
		titulo=doc.findall("events/event/title")
		empezar=doc.findall("events/event/start_time")

	return template('formulario.tpl', titulo=titulo, ciudad=ciudad, tipo=tipo, empezar=empezar)



@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])


