1. Start the venv environment with `. ./venv/bin/activate`
2. `python3 find.py -h` will show the help menu with the arguments and options.


```
(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % find ../ex5 -name "*.txt" -print 
../ex5/combined.txt
../ex5/c.txt
../ex5/b.txt
../ex5/a.txt
../ex5/d.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py ../ex5 -n "*.txt" -p
../ex5/combined.txt
../ex5/c.txt
../ex5/b.txt
../ex5/a.txt
../ex5/d.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py ../ex5 -n "*.txt" --print
../ex5/combined.txt
../ex5/c.txt
../ex5/b.txt
../ex5/a.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % find .. -name "*.txt" -print                
../venv/lib/python3.11/site-packages/pip/_vendor/vendor.txt
../venv/lib/python3.11/site-packages/setuptools-65.6.3.dist-info/entry_points.txt
../venv/lib/python3.11/site-packages/setuptools-65.6.3.dist-info/top_level.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/entry_points.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/top_level.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/LICENSE.txt
../ex5/combined.txt
../ex5/c.txt
../ex5/b.txt
../ex5/a.txt
../ex5/d.txt

dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py . -n "*.md" --exec "ls" 
README.md       __pycache__     example.py      find.py
```
## example.py
Sameple python file from geeksforgeeks example on how to print all files within a directory.
https://www.geeksforgeeks.org/how-to-print-all-files-within-a-directory-using-python/#
os.startfile() only works on Windows Operating system though.

## glob
Good for recursively getting filepaths and dirpaths
https://docs.python.org/3/library/glob.html