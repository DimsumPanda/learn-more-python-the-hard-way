import argparse
import re

def sed():
    parser = argparse.ArgumentParser(description='stream editor. Reads the specified files, modifies the input as specified by a list of commands.')
    parser.add_argument('-a', '--text_to_alter', help='text to alter')
    parser.add_argument('-r', '--text_to_replace_with', help='text to replace')
    parser.add_argument('-o','--outputfile', help='output file with modified content')
    parser.add_argument('-f','--file', help='file to modify', required=True)
    args = parser.parse_args()
    # If there is not output file, then save file as the original file.
    if args.outputfile:
        outputfile = args.outputfile
    else:
        outputfile = args.file
    replace_word_in_file(args.text_to_alter, args.text_to_replace_with, args.file, outputfile)

# Make outputfile optional by passing in the None default
def replace_word_in_file(text_to_alter, text_to_replace_with, file, output_file=None):
    if output_file is None:
        output_file = file
    with open(file, 'r') as f:
        file_content = f.read()
    
    # 'w' will overwrite any existing file.
    # 'a' will append to the end of the file.
    with open(output_file, 'w') as f:
        regexToAlter = re.compile(f'{text_to_alter}')
        new_content = regexToAlter.sub(text_to_replace_with, file_content)
        f.write(new_content)

if __name__ == '__main__':
    sed()
    