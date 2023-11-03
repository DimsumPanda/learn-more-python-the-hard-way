# uniq

## Comparison of uniq.py and uniq
```
% history | sed -e "s/^[ 0-9]*//g" | cut -d ' ' -f 1 | python3 uniq.py
cat
cd
history
% history | sed -e "s/^[ 0-9]*//g" | cut -d ' ' -f 1 | uniq           
cat
history
cd
history

# -c adds the count in front of the item.
dimsumpanda@dimsumpandas-MacBook-Pro ex11-uniq % history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -c
1 history
1 history | sed -e "s/^[ 0-9]*//g"
1 history | sed -e "s/^[ 0-9]*//g" |  python3 uniq.py
2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py
2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -c
2 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq
1 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -c
2 history | sed -e "s/^[ 0-9]*//g" |  uniq
1 history | sed -e "s/^[ 0-9]*//g" | cut -w -f 1 | python3 uniq.py
1 history | sed -e "s/^[ 0-9]*//g" | cut -w -f 1 | uniq
dimsumpanda@dimsumpandas-MacBook-Pro ex11-uniq % history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -c           
   1 history | sed -e "s/^[ 0-9]*//g"
   1 history | sed -e "s/^[ 0-9]*//g" |  python3 uniq.py
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py
   3 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -c
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq
   1 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -c
   2 history | sed -e "s/^[ 0-9]*//g" |  uniq
   1 history | sed -e "s/^[ 0-9]*//g" | cut -w -f 1 | python3 uniq.py
   1 history | sed -e "s/^[ 0-9]*//g" | cut -w -f 1 | uniq

## Adding the -dc flag which adds counts in front of duplicated items.
% history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -dc
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py
   3 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -c
   2 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq
   3 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -c

% history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -dc
2 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
3 history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -c
2 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq
3 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -c
2 history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -dc

# -u for unique items only
% history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -u 
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -dc
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -Dc
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -d

% history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -u           
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -dc
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -u
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -Dc
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -d

# Output all lines that are repeated (-D)
% history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
cat a.txt b.txt c.txt > combined_cat.txt
cd ../ex11-uniq
cd ../ex6-find
find.py . -n "*.md" --exec "ls" 
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D
python3 cat.py "a.txt b.txt c.txt" -o combined_pycat.txt
python3 cat.py "a.txt b.txt c.txt" > combined_pycat.txt
python3 find.py -h
python3 find.py . -n "*.md" --exec "ls" 

% history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D           
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
history | sed -e "s/^[ 0-9]*//g" |  sort | python3 uniq.py -D
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D
history | sed -e "s/^[ 0-9]*//g" |  sort | uniq -D
python3 cat.py "a.txt b.txt c.txt" -o combined_pycat.txt
python3 cat.py "a.txt b.txt c.txt" -o combined_pycat.txt
```

## Exercise to use sed, cut, sort, and uniq python scripts
In the exercise, the challenge asks us to recreate the following bash statement in python
using what we learned in the previous exercises:
`history | sed -e "s/^[ 0-9]*//g" | cut -d ' ' -f 1 | sort | uniq`

```
% history | sed -e "s/^[ 0-9]*//g" | cut -d ' ' -f 1 | sort | uniq
cat
history
ls
% history | python3 sed.py -a "^[0-9]*" -r "" | python3 cut.py -d ' ' -f 1 | python3 sort.py | python3 uniq.py
 
cat
history
ls
```
