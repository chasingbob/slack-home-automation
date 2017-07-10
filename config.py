import json

def get_value(name):
	'''Get the value from a json config file

		# Args:
			name of the value
	'''
	with open('config.json', 'r') as f:
		config = json.load(f)
	    return config[name]

