# Cut

```
dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | python3 cut_sys.py -f 1-2 -w
total 32
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
-rw-r--r-- 1
dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | cut -f 1-2 -w
total   32
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1
-rw-r--r--      1

dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | python3 cut_sys.py -f 3-5 -d ' '
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda

dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | cut -f 3-5 -d ' '               

1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 
1 dimsumpanda 

dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | python3 cut_sys.py -f 1-5 -d ' '
total 40
 -rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
dimsumpanda@dimsumpandas-MacBook-Pro ex8-cut % ls -l | cut -f 1-5 -d ' '              
total 40
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 
-rw-r--r--  1 dimsumpanda 

```