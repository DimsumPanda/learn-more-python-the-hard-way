```
% python3 grep.py "a\.txt" "../ex05-cat/*.txt"
../ex05-cat/combined_pycat.txt:I am a.txt
../ex05-cat/a.txt:I am a.txt
../ex05-cat/combined_cat.txt:I am a.txt

% grep a.txt ../ex05-cat/*.txt   
../ex05-cat/a.txt:I am a.txt
../ex05-cat/combined_cat.txt:I am a.txt
../ex05-cat/combined_pycat.txt:I am a.txt
```
Also added grep as a local module to find.py
```
% python3 find.py ../ex05-cat -n "*.txt" --grep "am" 
../ex05-cat/combined.txt:I am a.txt
../ex05-cat/combined.txt:I am b.txt
../ex05-cat/combined.txt:I am c.txt
../ex05-cat/combined.txt:I am d.txt
../ex05-cat/combined.txt:I am c.txt
../ex05-cat/c.txt:I am c.txt
../ex05-cat/b.txt:I am b.txt
../ex05-cat/a.txt:I am a.txt
../ex05-cat/d.txt:I am a.txt
../ex05-cat/d.txt:I am b.txt
../ex05-cat/d.txt:I am c.txt
../ex05-cat/d.txt:I am d.txt
```
All I had to do was create a function within `grep.py` and then import it in `find.py`.
Of course, I also needed `if __name__ = "__main__":` for it to be a module.