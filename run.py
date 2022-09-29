#!/usr/bin/env python

from argparse import ArgumentParser
import os
import subprocess

parser = ArgumentParser()
parser.add_argument('-r', '--release', '--production', 
                    action='store_true', dest='is_release', default=False, 
                    help='Runs the app publicly. Only use this in production or if you trust the users on your network.')
parser.add_argument('-s', '--ssl', '--https', 
                    action='store_true', dest='ssl_cert', default=False, 
                    help='Enables HTTPS with a signed-certificate. Note that it\'s hard-coded to look for the files \'cert.pem\' and \'key.pem\'.')
args = parser.parse_args()

# enables us to open relative paths
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('src')

host = '127.0.0.1'
debug = '--debug'

if args.is_release:
    host = '0.0.0.0'
    debug = '--no-debug'

if args.ssl_cert:
    subprocess.run(["flask", debug, "run", 
                    f"--host={ host }", 
                    "--cert=cert.pem", 
                    "--key=key.pem"])
else:
    subprocess.run(["flask", debug, "run", 
                    f"--host={ host }"])
