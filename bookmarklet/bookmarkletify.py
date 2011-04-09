#!/usr/bin/python

def bookmarkletify(jstext):
	import urllib
	return urllib.quote(jstext.strip())

def create_from_template(jstext):
	html = \
"""<html>
	<head>
	</head>

	<body>
		<a href="javascript:{0}">{1}</a>
	</body>
</html>"""
	text = "Bookmarklet"
	return html.format(bookmarkletify(jstext),text)

def main():
	import sys

	if len(sys.argv) < 2:
		print "Usage: {0} filename".format(sys.argv[0])
		return

	jstext = open(sys.argv[1]).read()

	#print bookmarkletify(jstext)
	print create_from_template(jstext)

if __name__ == "__main__":
	main()
