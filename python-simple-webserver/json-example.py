#!/usr/bin/env python3

"""
An example of how to use the json module.
This module is also really simple, it is used to parse json into a dict,
amongest many other things.
"""
import json

jsonData = '{"name": "Paulo", "age": 21, "race": "sleepy mexican", "height": 71}'
jsonDict = json.loads(jsonData)
print(jsonDict)
print(type(jsonDict) is dict)

for key in jsonDict:
    print(key, jsonDict[key])
