# -*- coding: utf-8 -*-

"""Quickly lanuch a temporary Firefox instance."""

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Firefox temporary profile"
__version__ = "1.0.0"
__trigger__ = "fx"
__author__ = "Benjamin Altpeter"
__dependencies__ = []

iconPath = iconLookup("firefox")

def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    results.append(
        Item(
            id=__prettyname__,
            icon=iconPath,
            text="Launch temporary Firefox profile",
            subtext="This will create a new temporary Firefox profile and launch an instance with it.",
            completion=query.rawString,
            actions=[
                # Command taken from: https://news.ycombinator.com/item?id=18898865
                FuncAction("Launch temporary Firefox", lambda: os.system("firefox --new-instance --profile $(mktemp -d) &"))
            ]
        )
    )

    return results
