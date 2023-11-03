import argparse
import sys
import random

def parse_arguments():
    parser = argparse.ArgumentParser(description='sort or merge records (lines) of text and binary files')
    parser.add_argument('-r', '--reverse', action='store_true', help='reverse the sorted list')
    parser.add_argument('-f', '--ignore_case', action='store_true', help='Convert all lower case characters to their uppercase equivalent before comparison.')
    parser.add_argument('-R', '--random_sort', action='store_true', help='Sort by a random order')
    parser.add_argument('--version', action='version', version='2.3-Apple (154)')
    return parser.parse_args()

def main():
    args = parse_arguments()
    # Take the stdin as the list
    unsorted_list = [line.strip() for line in sys.stdin]
    if args.ignore_case:
        sorted_list = sorted(unsorted_list, reverse=args.reverse, key=lambda x: x.upper())
    elif args.random_sort:
        sorted_list = random.sample(unsorted_list, len(unsorted_list))
        # random.shuffle - shuffles in place.
    else:
        sorted_list = sorted(unsorted_list, reverse=args.reverse)
        
    for line in sorted_list:
        print(line)

if __name__ == '__main__':
    main()