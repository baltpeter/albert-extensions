# -*- coding: utf-8 -*-

"""Issue DNS requests through Albert."""

from albertv0 import *
import subprocess
import ipaddress

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Dig"
__version__ = "1.0.0"
__trigger__ = "dig"
__author__ = "Benjamin Altpeter"
__dependencies__ = []

defaultIcon = iconLookup("network-server")

def handleQuery(query):
    if not query.isTriggered:
        return

    results = []
    args = query.string.split()

    if len(args) > 0:
        try:
            cmd = ["dig", "+noall", "+noclass", "+answer"]
            if isIp(args[0]): cmd.append("-x")
            cmd.append(args[0])
            if len(args) > 1: cmd.append(args[1])

            sp = subprocess.run(cmd, stdout=subprocess.PIPE)
            output = list(map(lambda line: line.split(), sp.stdout.decode("utf-8").split("\n")))

            for line in output:
                if len(line) > 3:
                    value = " ".join(line[3:])

                    results.append(
                        Item(
                            id=__prettyname__,
                            icon=defaultIcon,
                            text=value + " :: " + line[2],
                            subtext=line[0] + " :: TTL = " + line[1],
                            completion=value,
                            actions=[
                                ClipAction("Copy value", value)
                            ]
                        )
                    )
        except:
            pass
    else:
        results.append(
            Item(
                id=__prettyname__,
                icon=defaultIcon,
                text="Enter your query to lookup DNS records.",
                subtext="First argument is the domain or IP, (optional) second argument is the record type.",
                completion=query.rawString
            )
        )

    return results

def isIp(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except: return False
