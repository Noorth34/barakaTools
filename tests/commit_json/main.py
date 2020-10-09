#coding:utf-8

import json
from datetime import datetime, date

log = None

message = str(raw_input("Type your commit message here... : "))

commit = {
	"Date" : str(date.today()),
	"Time" : str(datetime.now().time().strftime("%H:%M:%S")),
	"Commit" : message
}


def write_json(data, filename="commits.json"):
	with open(filename, "w") as f:
		json.dump(data, f, indent=4)

def print_logs(data):
	"""
	"""


if __name__ == "__main__":

	with open("commits.json") as f:
		
		data = json.load(f)
		temp = data["logs"]
		temp.append(commit)

	write_json(data)






