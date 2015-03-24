#!/usr/bin/env python
# -*- coding: UTF8 -*-
import re

from flask import Flask, request
from question import QUESTIONS

app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print q
    response = ''

    for (pattern, func) in QUESTIONS:
        match = re.search(pattern, q)
        if match:
            response = str(func(match.groups()))
            break

    print '==> ' + response
    return response

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

