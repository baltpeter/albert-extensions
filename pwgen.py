# -*- coding: utf-8 -*-

"""Generate passwords of a specified length."""

from albert import *
import string
import secrets

__title__ = "Password generator"
__version__ = "0.4.1"
__triggers__ = "pw"
__authors__ = "Benjamin Altpeter"

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
			id=__title__,
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
