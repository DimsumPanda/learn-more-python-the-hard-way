import argparse
import re

parser = argparse.ArgumentParser(description='cut out selected portions of each line of a file')
# parser.add_argument('list', help='comma or whitespace separated set of numbers and/or number rnages.')
# parser.add_argument('-b', help='The list specifies byte positions.')
# parser.add_argument('-c', help='The list specifies character positions.')
parser.add_argument('-d', '--delim', help='Use delim as the field delimiter character instead of the tab character.')
parser.add_argument('-f', '--fields', help='The list specifies fields, separated in the input by the field delimiter character (see the -d option). Output fields are separated by a single occurrence of the field delimiter character.')
parser.add_argument('-w', '--whitespace', action='store_true', help='Use whitespace (spaces and tabs) as the delimiter. Consecutive spaces and tabs count as one single field separater')


list = """drwxr-xr-x  5 dimsumpanda  staff  160 Sep 26 17:41 ex4
drwxr-xr-x  9 dimsumpanda  staff  288 Sep 28 17:03 ex5
drwxr-xr-x  6 dimsumpanda  staff  192 Oct 30 21:10 ex6
drwxr-xr-x  6 dimsumpanda  staff  192 Oct 30 21:19 ex7
drwxr-xr-x  3 dimsumpanda  staff   96 Oct 31 09:24 ex8-cut
drwxr-xr-x  6 dimsumpanda  staff  192 Jul  4 17:07 venv"""

if __name__ == '__main__':
    args = parser.parse_args()

    if args.fields:
        for row in list.split('\n'):
            if args.delim:
                # split_row_without_delim = row.split(args.delim)
                # split_row = []
                # for x in split_row_without_delim:
                #     split_row.append(x)
                #     split_row.append(args.delim)
                split_row = re.split(f"{args.delim}", row)
                # print(split_row)
            elif args.whitespace:
                split_row = row.split()
            else:
                print("-f (--fields) need -d delim. -d (--delim) is missing.")

            # print(split_row)
            # print out only the range in fields
            if '-' in args.fields:                
                fields_split = args.fields.split('-')
                for i in range(int(fields_split[0])-1, int(fields_split[1])):
                    # print("i is: ", i)
                    if i == int(fields_split[1])-1:
                        print(split_row[i])
                    else:
                        print(split_row[i], end = " ")
            else:
                print(split_row[int(args.fields)-1], end=" ")

            