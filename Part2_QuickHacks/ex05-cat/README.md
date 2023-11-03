# Exercise 5 - Cat
Simple cat.py that can print out content in a text and combine text documents.

```
# Print out text in a file
% cat a.txt
I am a.txt

% python3 cat.py a.txt
I am a.txt

# Combine text into a new document
% cat a.txt b.txt c.txt > combined_cat.txt
Output:
I am a.txt
I am b.txt
I am c.txt

% python3 cat.py "a.txt b.txt c.txt" -o combined_pycat.txt
I am a.txt
I am b.txt
I am c.txt

```