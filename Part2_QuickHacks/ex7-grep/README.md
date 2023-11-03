```
dimsumpanda@dimsumpandas-MacBook-Pro learn-more-python-the-hard-way % python3 ex7/grep.py "a\.txt" "ex5/*.txt"
ex5/combined.txt:I am a.txt
ex5/a.txt:I am a.txt
ex5/d.txt:I am a.txt

dimsumpanda@dimsumpandas-MacBook-Pro learn-more-python-the-hard-way % grep am ex5/*.txt   
ex5/a.txt:I am a.txt
ex5/b.txt:I am b.txt
ex5/c.txt:I am c.txt
ex5/combined.txt:I am a.txt
ex5/combined.txt:I am b.txt
ex5/combined.txt:I am c.txt
ex5/combined.txt:I am d.txt
ex5/combined.txt:I am c.txt
ex5/d.txt:I am a.txt
ex5/d.txt:I am b.txt
ex5/d.txt:I am c.txt
ex5/d.txt:I am d.txt
dimsumpanda@dimsumpandas-MacBook-Pro learn-more-python-the-hard-way % python3 ex7/grep.py "am" "ex5/*.txt"
ex5/combined.txt:I am a.txt
ex5/combined.txt:I am b.txt
ex5/combined.txt:I am c.txt
ex5/combined.txt:I am d.txt
ex5/combined.txt:I am c.txt
ex5/c.txt:I am c.txt
ex5/b.txt:I am b.txt
ex5/a.txt:I am a.txt
ex5/d.txt:I am a.txt
ex5/d.txt:I am b.txt
ex5/d.txt:I am c.txt
ex5/d.txt:I am d.txt
```
Also added it as a local module to find.
```
(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex7 % python3 find.py ../ex5 -n "*.txt" --grep "am" 
../ex5/combined.txt:I am a.txt
../ex5/combined.txt:I am b.txt
../ex5/combined.txt:I am c.txt
../ex5/combined.txt:I am d.txt
../ex5/combined.txt:I am c.txt
../ex5/c.txt:I am c.txt
../ex5/b.txt:I am b.txt
../ex5/a.txt:I am a.txt
../ex5/d.txt:I am a.txt
../ex5/d.txt:I am b.txt
../ex5/d.txt:I am c.txt
../ex5/d.txt:I am d.txt
```
All I had to do was create a function within `grep.py` and then import it in `find.py`.
Of course, I also needed `if __name__ = "__main__":` for it to be a module.