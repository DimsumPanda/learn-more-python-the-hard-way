import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='report or filter out repeated lines in a file')
    parser.add_argument('-c', '--count', action='store_true', help='Precede each output line with the count of the number of times the line occurred in the input, followed by a single space.')
    parser.add_argument('-d', '--repeated', action='store_true', help='Output a single copy of each line that is repeated in the input')
    parser.add_argument('-D', '--all_repeated', action='store_true', help='Output all lines that are repeated.')
    parser.add_argument('-u', '--unique', action='store_true', help='Only output lines that are not repeated in the input.')
    parser.add_argument('-i', '--ignore_case', action='store_true', help='Case insensitive comparison of lines.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # # Take stdin piped information and find the unique set and print it out
    # # set is unordered though, so it will not keep the order of its input.
    # unique_list = set(sys.stdin)
    # for x in unique_list:
    #     print(x, end="")
    original_input = sys.stdin

    uniqueList, countdict = get_ordered_list(original_input, args.ignore_case)

    for item in uniqueList:
        if args.repeated:
            if countdict.get(item) > 1:
                print_line(item, countdict, args.count)
        elif args.unique:
            if countdict.get(item) == 1:
                print_line(item, countdict, args.count)
        else:
            print_line(item, countdict, args.count)
    if args.all_repeated:
        for line in original_input:
            if (line in uniqueList) and countdict.get(line) > 1:
                print_line(line, countdict, args.count)

def print_line(item, countdict, getCount=False):
    if getCount:
        print(f'{countdict.get(item)} {item}')
    else:
        print(f'{item}')

def get_ordered_list(list, ignoreCase=False):
    countdict = {}
    uniqueList = []
    for x in list:
        item = x.strip()
        if ignoreCase:
            if item.lower() in countdict.keys():
                # increase the count_dict
                countdict[item.lower()] += 1
            else:
                # insert the item as key with count = 1
                countdict[item.lower()] = 1
        else:
            if item in countdict.keys():
                # increase the count_dict
                countdict[item] += 1
            else:
                # insert the item as key with count = 1
                countdict[item] = 1
    for key in countdict.keys():
        uniqueList.append(key)
    return uniqueList, countdict


if __name__ == '__main__':
    main()