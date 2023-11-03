# Sort
sort or merge records (lines) of text and binary files.

```
% ls | sort
README.md
sort.py
% ls | python3 sort.py           
README.md
sort.py

% cat unsorted.txt | sort
cheap
elegant
exchange
fairy
lemon
muscle
parking
shelf
specimen
variety

% cat unsorted.txt | python3 sort.py 
cheap
elegant
exchange
fairy
lemon
muscle
parking
shelf
specimenvariety

# Reverse the sorted list
% cat unsorted.txt | python3 sort.py -r
variety
specimenshelf
parking
muscle
lemon
fairy
exchange
elegant
cheap

% cat unsorted.txt | sort -r
variety
specimen
shelf
parking
muscle
lemon
fairy
exchange
elegant
cheap

# Ignore case when sorting
% cat unsorted.txt | python3 sort.py -f
cheap
elegant
exchange
fairy
Fart
lemon
muscle
parking
shelf
specimen
variety

% cat unsorted.txt | sort -f   
cheap
elegant
exchange
fairy
Fart
lemon
muscle
parking
shelf
specimen
variety

# Practicing version action in argparse 
% sort --version
2.3-Apple (154)
% python3 sort.py --version
2.3-Apple (154)

# Randomize the list
% cat unsorted.txt | python3 sort.py -R
exchange
parking
cheap
shelf
elegant
variety
muscle
Fart
lemon
specimen
fairy
```