import argparse
import re
import glob

parser = argparse.ArgumentParser(description='file pattern searcher')
parser.add_argument('pattern', help='pattern to match')
parser.add_argument('file', help='file or regex for files to search for')

def print_matching_content(regexpattern, filepattern):
    files_list = glob.glob(filepattern, recursive=True)

    patternRegex = re.compile(regexpattern)
    for file in files_list:
        with open(file, 'r') as f:
            file_content = f.readlines()
            for line in file_content:
                if patternRegex.search(line):
                    # So there isn't a weird newline
                    print(f'{file}:{line}', end="")

if __name__ == "__main__":
    args = parser.parse_args()
    print_matching_content(args.pattern, args.file)