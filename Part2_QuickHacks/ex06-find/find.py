import argparse
import os
import subprocess
import glob

parser = argparse.ArgumentParser(description='walk a file hierarchy')
parser.add_argument('-n', '--name', help='True if the last component of the pathname being examined matches pattern. Special shell pattern matching characters ("[", "]", "*", and "?") may be used as part of pattern. These characters may be matched explicitly by escaping them with a backslack ("\\").')
parser.add_argument('-p', '--print', action='store_true', help='This primary always evaluates to true. It prints the pathname of the current file to standard output. If none of -exec, -ls, -print, -print0, or -ok is specified, the given expression shall be effectively replaced by (given expression) -print.')
parser.add_argument('-t', '--type', help='True if the file is of the specified type. Possible file types: \n d  directory')
parser.add_argument('--exec', help='True if the argument returns a zero value as its exit status.')
parser.add_argument('dirpath', help='directory path to search in')


if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.name:
        files_list = glob.glob(f"**/{args.name}", root_dir=args.dirpath, recursive=True)
    else:
        files_list = glob.glob("**/*", root_dir=args.dirpath, recursive=True)

    for file in files_list:
        full_file_path = f'{args.dirpath}/{file}'
        if (not args.type or (args.type == "d" and os.path.isdir(file))):
            if args.print:
                print(full_file_path)
            if args.exec:
                subprocess.run([f"{args.exec} {full_file_path}"], shell=True, check=True)