# Ex13: Single Linked Lists

## Prerequisites
If you haven't already, install venv and the requirements (e.g. pytest).
```
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

## Run Tests

You can either run `pytest` which will run run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard [https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#test-discovery](test discovery rules).
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
% python3 -i test_sllist.py
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
rootdir: learn-more-python-the-hard-way/Part3_DataStructuresAndAlgorithms/ex13-single-linked-lists
collected 8 items                                                                                                                                     

test_sllist.py ....before perinone:
Zinc White Nickle Yellow Perinone 

after perinone:
Zinc White Nickle Yellow 
```
Documentation on `pytest -s` can be found in the docs: https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html
## Helpful Resources
Some relevant resources for completing Exercise 13: Single Linked Lists:
- pytest - https://docs.pytest.org/en/7.4.x/
- Author's rough solution (not a full solution to get you started): https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/tree/master/ex13_sllist
- [https://docs.python.org/3/tutorial/classes.html](Python Classes Documentation)
- [RealPython article on Writing Test](https://realpython.com/python-testing/#writing-your-first-test)