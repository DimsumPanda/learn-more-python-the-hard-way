import argparse
import os

parser = argparse.ArgumentParser(description='This program uses argparse.py')

parser.add_argument('-a', '--enable_agent', help="Enables monitoring agent", action="store_true")
parser.add_argument('-m', '--enable_metrics', help="Enables datadog metrics", action="store_true")
parser.add_argument('-x', '--enable_health', help="Enable health endpoint for loadbalancer", action="store_true")
parser.add_argument('-f', '--first_name', help="first name")
parser.add_argument('-l', '--last_name', help="last name")
parser.add_argument('-p', help="Port for service to run on")
parser.add_argument('file_path')

args = parser.parse_args()

if args.enable_agent:
    print("Agent is enabled")
if args.enable_metrics:
    print("Metrics are enabled")
if args.enable_health:
    print("Health check enabled")
if args.first_name:
    print(f"First Name: {args.first_name}")
if args.last_name:
    print(f"Last Name: {args.last_name}")
# When there is no long-form flag, you can use the letter for the flag.
if args.p:
    print(f"Port: {args.p}")
if args.file_path:
    with os.scandir(args.file_path) as files:
        for file in files:
            print(file.name)