from argparse import ArgumentParser
import os
import requests
from datetime import datetime
import subprocess

parser = ArgumentParser(description = "Read in a system service name")
parser.add_argument("serviceName", help="A service name should be passed to me, shame if it's not.")
args = parser.parse_args()

errString = "**{}** has failed!".format(args.serviceName)
anotherExec = "status -l -n 15 {}".format(args.serviceName)
errDesc = subprocess.run(['systemctl', 'status', '-l', '-n 15', args.serviceName], stdout = subprocess.PIPE).stdout.decode('utf-8')

message = {
	'content': "<@156872400145874944>",
	"embeds": [{
		'title': errString,
		'description': "Wake up, your thing broke (and it should have restarted by now - but here's the status on failure...)",
		'color': 790027,
		'timestamp': datetime.utcnow().isoformat()
	},
	{
		'title': "Status",
		'description': errDesc,
        'color': 13185600
	}]
}
URL = ""
r = requests.post(URL, json = message)
