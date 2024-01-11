1. Start the venv environment with `. ./venv/bin/activate`
2. `python3 find.py -h` will show the help menu with the arguments and options.


```
(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % find ../ex05-cat -name "*.txt" -print 
../ex05-cat/combined.txt
../ex05-cat/c.txt
../ex05-cat/b.txt
../ex05-cat/a.txt
../ex05-cat/d.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py ../ex05-cat -n "*.txt" -p
../ex05-cat/combined.txt
../ex05-cat/c.txt
../ex05-cat/b.txt
../ex05-cat/a.txt
../ex05-cat/d.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py ../ex05-cat -n "*.txt" --print
../ex05-cat/combined.txt
../ex05-cat/c.txt
../ex05-cat/b.txt
../ex05-cat/a.txt

(venv) dimsumpanda@dimsumpandas-MacBook-Pro ex6 % find .. -name "*.txt" -print                
../venv/lib/python3.11/site-packages/pip/_vendor/vendor.txt
../venv/lib/python3.11/site-packages/setuptools-65.6.3.dist-info/entry_points.txt
../venv/lib/python3.11/site-packages/setuptools-65.6.3.dist-info/top_level.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/entry_points.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/top_level.txt
../venv/lib/python3.11/site-packages/pip-22.3.1.dist-info/LICENSE.txt
../ex05-cat/combined.txt
../ex05-cat/c.txt
../ex05-cat/b.txt
../ex05-cat/a.txt
../ex05-cat/d.txt

dimsumpanda@dimsumpandas-MacBook-Pro ex6 % python3 find.py . -n "*.txt" --exec "ls -l"   
-rw-r--r--  1 dimsumpanda  staff  0 Nov  1 10:24 ./a.txt
```
## example.py
Sample python file from geeksforgeeks example on how to print all files within a directory.
https://www.geeksforgeeks.org/how-to-print-all-files-within-a-directory-using-python/#
os.startfile() only works on Windows Operating system though.

## glob
Good for recursively getting filepaths and dirpaths
https://docs.python.org/3/library/glob.html