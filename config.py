import json

def get_value(name):
	with open('config.json', 'r') as f:
		config = json.load(f)
		return config[name]

