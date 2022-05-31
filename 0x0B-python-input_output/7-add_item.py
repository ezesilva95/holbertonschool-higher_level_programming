#!/usr/bin/python3
'''
Module 7. Load, add, save
'''


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = "add_item.json"

try:
    data = load_from_json_file(f)
except FileNotFoundError:
    load = []

save_to_json_file(data + argv[1:], f)
