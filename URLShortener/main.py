# main.py

from flask import Flask
from flask import request
from flask import jsonify
import hashlib
import inspect

app = Flask(__name__)

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

_usage = '<h1>Welcome to a URLShortener demo </h1>' \
		'<h2>You can use the APIs to generate a shorturl by URL, APIs as following</h2>' \
		'<h3>/create?url=URL</h3>' \
		'<h3>/preview?shorturl=shorturl</h3>' \
		'<h3>/list</h3>'

# class URLShortener Definition
class URLShortener():
	def __init__(self, ServiceHost='http://localhost/', debug=False):
		self.ServiceHost = ServiceHost
		self.debug = debug
		self.ShortURL_dict = {}
		self.AlnumList = []
		for char in '0123456789ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz':
			self.AlnumList.append(char)
		self.DP(lineno(), 'Debug Mode Enable')

	# Debug Print
	def DP(self, line, msg):
		if self.debug == True:
			print('[DEBUG:%3s] %s' % (line, msg))

	def GenShortURL(self, URL):
		if URL[0:8] != 'http://' and URL[0:8] != 'https://':
			self.DP(lineno(), 'The URL(%s) miss http:// or https://' % URL)
			URL = 'http://' + URL

		hexstr = hashlib.sha256(URL.encode('UTF-8')).hexdigest()[0:16]
		self.DP(lineno(), 'Get first 16 bytes of sha256(%s)=%s' % (URL, hexstr))

		ShortURL = ''.join(self.AlnumList[int(hexstr[i:i+2], 16) % len(self.AlnumList)] for i in range(0, len(hexstr), 2))
		self.DP(lineno(), 'Convert(%s) to ShortURL(%s) ' % (hexstr, ShortURL))

		self.ShortURL_dict[ShortURL] = URL
		return ShortURL

	def GetURL(self, ShortURL):
		return self.ShortURL_dict.get(ShortURL, None)


@app.route("/")
def index():
	return _usage

# Convert from URL to shorturl
@app.route("/create")
def create():
	hostname = request.args.get('url', default=None)
	if hostname is None:
		return '<h1>Please give a url to shorturl, format is<br/> /create?url=http://your_url/</h1>'
	else:
		return us.ServiceHost + us.GenShortURL(hostname)

# Convert shorturl to URL
@app.route("/<string:shorturl>")
def forward(shorturl):
	URL = us.GetURL(shorturl)
	if URL is None:
		return '<h1>The shorturl is not found</h1>'
	else:
		return '<html><script> window.location.replace("' + URL + '");</script>'

# Don't forward URL immediately, show URL to user
@app.route("/preview")
def preview():
	shorturl = request.args.get('shorturl', default=None)

	if shorturl is None:
		return '<h1>Please give a shorturl</h1>'

	URL = us.GetURL(shorturl)
	if URL is None:
		return '<h1>The shorturl is not found</h1>'
	else:
		return URL

# give a di
@app.route("/list")
def list():
	return jsonify(us.ShortURL_dict)

if __name__ == "__main__":
	print(' * URLShortener Demo start!')
	us = URLShortener(ServiceHost='http://localhost:5000/', debug=True)
	# us = URLShortener(ServiceHost='http://localhost:5000/')

	# test data
	us.GenShortURL('https://www.google.com')
	us.GenShortURL('https://twitter.com')
	us.GenShortURL('http://www.reddit.com')
	us.GenShortURL('www.facebook.com')
	us.GenShortURL('www.yahoo.com.tw/')
	us.GenShortURL('testdata')
	us.GenShortURL('https://github.com/tobypusheen')
	us.GenShortURL('http://localhost:5000/create?url=https://www.google.com.tw/search?q=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&oq=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&aqs=chrome..69i57.200j0j4&sourceid=chrome&ie=UTF-8')

	# shorturl is a hash like njwhgE6i, b1C4Vhse...etc,
	# it is generated by URL
	toby_linkedin = 'https://www.linkedin.com/in/toby-lin-b72025119/'
	shorturl = us.GenShortURL(toby_linkedin)
	us.DP(lineno(), 'Generate a shorturl ' + shorturl + ' by ' + toby_linkedin)

	# URL is a real website address can be accessed,
	# it may can be found by shorturl if it had generated
	URL = us.GetURL(shorturl)
	us.DP(lineno(), 'Find a URL ' + URL + ' by ' + shorturl)

	print(' * Show test data ')
	us.DP(lineno(), us.ShortURL_dict)

	app.run(debug=True, host='0.0.0.0', port='5000')

'''
Todo
	Documentation

TEST data
curl http://localhost:5000/create?url=http://www.google.com/
curl http://localhost:5000/create?url=http://www.yahoo.com.tw/
curl http://localhost:5000/create?url=https://www.ldoceonline.com/
curl http://localhost:5000/create?url=https://www.google.com.tw/search?q=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&oq=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&aqs=chrome..69i57.200j0j4&sourceid=chrome&ie=UTF-8

curl http://localhost:5000/list | jq

'''
