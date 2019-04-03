# -*- coding: utf-8 -*-

"""Generate passwords of a specified length."""

from albertv0 import *
import string
import secrets

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Password generator"
__version__ = "1.0.0"
__trigger__ = "pw"
__author__ = "Benjamin Altpeter"
__dependencies__ = []

iconPath = iconLookup("password")

def handleQuery(query):
	if not query.isTriggered:
		return

	length = 25
	try:
		length = int(query.string.strip())
	except:
		pass

	results = []

	pw = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))

	results.append(
		Item(
			id=__prettyname__,
	        icon=iconPath,
	        text=pw,
	        subtext="Your generated password of length " + str(length),
	        completion=pw,
	        actions=[
	            ClipAction("Copy URL", pw)
	        ]
        )
    )

	return results