# -*- coding: utf-8 -*-

"""Quickly open Flameshot to make a screenshot."""

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Flameshot shortcut"
__version__ = "1.0.0"
__trigger__ = "fs"
__author__ = "Benjamin Altpeter"
__dependencies__ = []

iconPath = iconLookup("flameshot")

def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    results.append(
        Item(
            id=__prettyname__,
            icon=iconPath,
            text="Open Flameshot in GUI mode",
            subtext="This will run `flameshot gui`.",
            completion=query.rawString,
            actions=[
                # We need to wait for the Albert prompt to disappear, otherwise it will be in the screenshot. Waiting for 0.2 seconds seems long enough but I am not sure. Maybe there is a cleaner way to do this?
                # We cannot use the more appropriate `ProcAction` here because (afaik) the subprocess.run-style array cannot issue commands like the one we want.
                FuncAction("Open Flameshot", lambda: os.system("(sleep 0.2 && flameshot gui)&"))
            ]
        )
    )

    return results
