# Cut

```
% ls -l | python3 cut_sys.py -f 1-2 -w
total 32
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
% ls -l | cut -f 1-2 -w
total   32
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1

% ls -l | python3 cut_sys.py -f 3-5 -d ' '
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda

% ls -l | cut -f 3-5 -d ' '               

1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 

% ls -l | python3 cut_sys.py -f 1-5 -d ' '
total 40
 -rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
% ls -l | cut -f 1-5 -d ' '              
total 40
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 

% ls -l | cut -f 9 -w               

README.md
cut.py
cut_sys.py
ls.txt
zed_example.py

% ls -l | python3 cut_sys.py -f 9 -w
README.md
cut.py
cut_sys.py
ls.txt
zed_example.py
```