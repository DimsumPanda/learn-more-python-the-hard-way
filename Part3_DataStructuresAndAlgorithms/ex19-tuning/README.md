# Ex19: Tuning
Leverages code found in: https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/tree/master/ex19_tuning


## Prerequisites
If you haven't already, install venv and the requirements (e.g. pytest).
```
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r ../requirements.txt
```

## Run Tests

Performance is faster than in ex18
```
% python3 -m cProfile -s cumtime test_sorting.py | grep sorting.py
        1    0.000    0.000    0.131    0.131 test_sorting.py:1(<module>)
        1    0.000    0.000    0.112    0.112 test_sorting.py:20(test_bubble_sort)
        1    0.107    0.107    0.107    0.107 sorting.py:1(bubble_sort)
        3    0.001    0.000    0.011    0.004 test_sorting.py:2(random_list)
        1    0.000    0.000    0.009    0.009 test_sorting.py:27(test_merge_sort)
        1    0.000    0.000    0.006    0.006 sorting.py:24(merge_sort)
        1    0.000    0.000    0.006    0.006 test_sorting.py:36(test_quick_sort)
   1599/1    0.001    0.000    0.006    0.006 sorting.py:32(merge_node)
 7536/799    0.004    0.000    0.004    0.000 sorting.py:60(merge)
        1    0.000    0.000    0.003    0.003 sorting.py:77(quick_sort)
   1063/1    0.000    0.000    0.003    0.003 sorting.py:81(quick_sort_doit)
      531    0.002    0.000    0.002    0.000 sorting.py:91(quick_sort_partition)
      799    0.001    0.000    0.001    0.000 sorting.py:15(count)
        3    0.000    0.000    0.000    0.000 test_sorting.py:9(is_sorted)
        1    0.000    0.000    0.000    0.000 sorting.py:1(<module>)
```



You can either run `pytest` which will run run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard [test discovery rules](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#test-discovery).
```
pytest
```
or you can specify the test file.
```
pytest test_<file_name>.py
```

## Debugging
For debugging, it's sometimes helpful to see print statements, e.g. in the `dump` function. 
In that case, I would run the test file as an interactive Python terminal, so I can see the full output:
```
% python3 -i test_dllist.py
>>> test_remove()
before perinone:
Zinc White Nickle Yellow Perinone 

after perinone:
Zinc White Nickle Yellow 
```
You can also pass `-s` to pytest to print out the stdout, even for passing tests:
```
% pytest -s                
================================================================= test session starts =================================================================
platform darwin -- Python 3.11.2, pytest-7.4.3, pluggy-1.3.0
rootdir: learn-more-python-the-hard-way/Part3_DataStructuresAndAlgorithms/ex14-double-linked-lists
collected 5 items                                                                                                                                     

test_dllist.py ....before perinone
[Zinc White, 'Nickle Yellow', None]
[Nickle Yellow, 'Perinone', 'Zinc White']
[Perinone, None, 'Nickle Yellow']
after perinone
[Zinc White, 'Nickle Yellow', None]
[Nickle Yellow, None, 'Zinc White']
.
```
Documentation on `pytest -s` can be found in the docs: https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html
## Helpful Resources
Some relevant resources for completing Exercise 17: Dictionary:
- pytest - https://docs.pytest.org/en/7.4.x/
- Author's rough solution (not a full solution to get you started): https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/tree/master/ex19_tuning
- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [RealPython article on Writing Test](https://realpython.com/python-testing/#writing-your-first-test)