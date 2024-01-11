# sed
Replaces a regex with a word using the `-r` flag.
```
%  python3 sed.py -f original.txt -o modified.txt -a "Level \w" -r "LEVEL OVER 9000"

% sed -e "s/Level [0-9]/LEVEL OVER 9000/g" original.txt > new.txt
```
## Original
```
Level 1 is having command line options for the most basic sed usage of replacing one string with another.
Level 2 is enabling regular expressions in those command line options.
Level 3 is implementing the sed expression format.
```
## Modified
```
LEVEL OVER 9000 is having command line options for the most basic sed usage of replacing one string with another.
LEVEL OVER 9000 is enabling regular expressions in those command line options.
LEVEL OVER 9000 is implementing the sed expression format.
```