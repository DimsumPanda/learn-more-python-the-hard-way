# Use plain old sys.argv
import sys
import getopt
import os
import glob

argv = sys.argv[1:]
first_name = ""
last_name = ""
port = ""
# Flags: agent, metrics, health-check
# Arguments: first_name, last_name, port
try:
    options, args = getopt.getopt(argv, "hamxf:l:p:",
                            ["help",
                            "enable-agent",
                            "enable-metrics",
                            "enable-health",
                            "first_name =",
                            "last_name =",
                            "port ="])
except:
    print("Error Message ")

for name, value in options:
    if name in ['-h', '--help']:
        print("This program uses sys.argv")
    elif name in ['-a', '--enable-agent']:
        print("agent is enabled")
    elif name in ['-m', '--enable-metrics']:
        print("Metrics are enabled")
    elif name in ['-x', '--enable-health']:
        print("Health check enabled")
    elif name in ['-f', '--first_name']:
        first_name = value
        print(f"First Name = {first_name}")
    elif name in ['-l', '--last_name']:
        last_name = value
        print(f"Last Name: {last_name}")
    elif name in ['-p', '--port']:
        port = value
        print(f"Port: {port}")
# List files in a given file path


if len(args) > 0:
    # with os.scandir(args[0]) as entries:
    #     for entry in entries:
    #         print(entry.name)
    files_match = glob.glob(args[0])
    print(files_match)