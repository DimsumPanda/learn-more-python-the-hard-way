import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='concatenate and print files')
    # parser.add_argument('-b', help="Number the non-blank output lines, starting at 1")
    # parser.add_argument('-e', help="Display non-printing characters (see the -v option), and display a dollar sign ('$') at the end of each line.")
    # parser.add_argument('-l', help="Set an exclusive advisory lock on the standard output file descriptor. This lock is set using fcntl(2) with the F_SETLKW command. If the output file is already locked, cat will block until the lock is acquired.")
    # parser.add_argument('-n', help="Number the output lines, starting at 1")
    # parser.add_argument('-s', help="Squeeze multiple adjacent empty lines, causing the output to be single spaced")
    # parser.add_argument('-t', help="Display non-printing characters (see the -v option), and display tab characters as '^I'.")
    # parser.add_argument('-u', help="Disable output buffering.")
    # parser.add_argument('-v', help="Display non-printing characters so they are visible. Control characters print as '^X' for control-X; the delete character (octal 0177) prints as '^?'. Non-ASCII characters (with the high bit set) are printed as 'M-' (for meta) followed by the character for the low 7 bits.")
    parser.add_argument('-o', '--output', help="outputfile of the combined files")
    parser.add_argument('files', help="string of files")

    args = parser.parse_args()

    # For each file in a string of files,
    # print the output of the file.
    output = ""
    for file in args.files.split(" "):
        with open(file, 'r') as f:
            # print(f.read())
            output += f.read()
    
    print(output)
    # If an output file is specified, save the output to that file path.
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)

