#!/usr/bin/python3.8

from jinja2 import Template

myDict= {'name': 'Felipe', 'Age' : '26'}

tmp = Template('Mi name is {{dic.name}} and i am {{dic.Age}} years old')
output = tmp.render(dic=myDict)
print(output)
