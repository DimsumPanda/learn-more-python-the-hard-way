import argparse
import re
import sys

parser = argparse.ArgumentParser(description='cut out selected portions of each line of a file')
parser.add_argument('-d', '--delim', help='Use delim as the field delimiter character instead of the tab character.')
parser.add_argument('-f', '--fields', help='The list specifies fields, separated in the input by the field delimiter character (see the -d option). Output fields are separated by a single occurrence of the field delimiter character.')
parser.add_argument('-w', '--whitespace', action='store_true', help='Use whitespace (spaces and tabs) as the delimiter. Consecutive spaces and tabs count as one single field separater')

if __name__ == '__main__':
    args = parser.parse_args()

    if args.fields:
        for line in sys.stdin:
            if args.delim:
                line_split = re.split(f"{args.delim}", line)
            elif args.whitespace:
                line_split = line.split()
            else:
                print("-f (--fields) need -d delim. -d (--delim) is missing.")

            # print out only the range in fields
            if '-' in args.fields:                
                fields_split = args.fields.split('-')
                if len(line_split) > int(fields_split[1]):
                    for i in range(int(fields_split[0])-1, int(fields_split[1])):
                        if i == int(fields_split[1])-1:
                            print(line_split[i])
                        else:
                            print(line_split[i], end = " ")
                elif len(line_split) > int(fields_split[0])-1:
                    for i in range(int(fields_split[0])-1, len(line_split)):
                        if i == len(line_split):
                            print(line_split[i])
                        else:
                            print(line_split[i], end = " ")
            else:
                if len(line_split) > int(args.fields):
                    print(line_split[int(args.fields)], end=" ")

            