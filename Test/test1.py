#!/usr/bin/python3.8

from jinja2 import Template

inputUser = input("Enter your name: ")

tmp = Template('Hello {{name}}')
msg = tmp.render(name = inputUser)

print(msg)