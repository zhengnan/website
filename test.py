#!/usr/bin/env python
from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
	def startElement(self, name, attrs):
		print name, attrs.keys()

	def endElement(self, name):
		print name

parse('website.xml', TestHandler())
