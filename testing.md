### Following Matt Rudge's Code Institute lectures...

Created byotest.py:

```
def f(object):
	return 0

def test_equal(actual, expected):
	assert expected  == actual, f'Expected {expected}, actual value returned was {actual}.'

test_equal(f(0),0)
```

Added another method:

```
def test_is_in(object, collection):
	assert object in collection, f'Expected {object} to be in {collection}, but it is not.'
```
Tested this with 

I am thinking about what I can test for and how I can cover as much of my code as possible with tests, ideally 100%.

#### Things to test for

- The login functionality works: a `userid` session object is created and the user is taken to problems.html
- The logout functionality works: a `userid` session object is destroyed and the user is taken to index.html
- For any user, the user object should be in the list of users
- If the user's answer is equal to the correct answer, the user's score should increase by one

#### Expanded byotest.py to:

```
# Beginnings of Python/Flask testing framework
# John Lynch
# January 2019

def f(object):
	return 0

arr = [2, 3, 5, 7, 11, 13, 17, 19]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_equal(actual, expected):
	assert expected  == actual, f'Expected {expected}, actual value returned was {actual}.'

def test_is_in(object, collection):
	assert object in collection, f'Expected {object} to be in {collection}, but it is not.'

def test_exists_as_session_object(obj):
	assert session.get("obj", False), f'{obj} is not currently saved as a session object.'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

test_equal(f(0),0)	# should pass

test_equal(f(1),1)	# should fail

test_is_in(7, arr)	# should pass

test_is_in(256, arr)	# should fail

test_exists_as_session_object(x) # should fail

session["x"] = 0

test_exists_as_session_object(x) # should pass

# 3 tests should fail out of 7
```
```
18:44 /arith: 2445$ git add testing.log byotest.py 
18:45 /arith: 2446$ git commit -m "Begin to create testing framework with byotest.py"
[master c8cde94] Begin to create testing framework with byotest.py
 2 files changed, 21 insertions(+)
 create mode 100644 byotest.py
 create mode 100644 testing.log
18:45 /arith: 2447$ python3 byotest.py 
19:09 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 14, in <module>
    test_is_in(8, arr)
  File "byotest.py", line 10, in test_is_in
    assert object in collection, f'Expected {object} to be in {collection}, but it is not.'
AssertionError: Expected 8 to be in [2, 3, 5, 7, 11, 13, 17, 19], but it is not.
19:09 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 5, in <module>
    obj = {name: "Bob", age: 30}
NameError: name 'name' is not defined
19:23 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 25, in <module>
    test_equal(f(1),1)	# should fail
  File "byotest.py", line 13, in test_equal
    assert expected  == actual, f'Expected {expected}, actual value returned was {actual}.'
AssertionError: Expected 1, actual value returned was 0.
19:31 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 29, in <module>
    test_is_in(256, arr)	# should fail
  File "byotest.py", line 16, in test_is_in
    assert object in collection, f'Expected {object} to be in {collection}, but it is not.'
AssertionError: Expected 256 to be in [2, 3, 5, 7, 11, 13, 17, 19], but it is not.
19:32 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 29, in <module>
    test_is_in(256, arr)	# should fail
  File "byotest.py", line 16, in test_is_in
    assert object in collection, f'Expected {object} to be in {collection}, but it is not.'
AssertionError: Expected 256 to be in [2, 3, 5, 7, 11, 13, 17, 19], but it is not.
19:32 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 31, in <module>
    test_exists_as_session_object(x) # should fail
NameError: name 'x' is not defined
19:32 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 32, in <module>
    test_exists_as_session_object(x) # should fail
  File "byotest.py", line 19, in test_exists_as_session_object
    assert session.get("obj", False), f'{obj} is not currently saved as a session object.'
NameError: name 'session' is not defined
19:33 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 5, in <module>
    from Flask import session
ModuleNotFoundError: No module named 'Flask'
19:34 /arith: 2448$ python3 byotest.py 
Traceback (most recent call last):
  File "byotest.py", line 34, in <module>
    test_exists_as_session_object(x) # should fail
  File "byotest.py", line 21, in test_exists_as_session_object
    assert session.get("obj", False), f'{obj} is not currently saved as a session object.'
  File "/usr/local/lib/python3.6/dist-packages/werkzeug/local.py", line 347, in __getattr__
    return getattr(self._get_current_object(), name)
  File "/usr/local/lib/python3.6/dist-packages/werkzeug/local.py", line 306, in _get_current_object
    return self.__local()
  File "/usr/local/lib/python3.6/dist-packages/flask/globals.py", line 37, in _lookup_req_object
    raise RuntimeError(_request_ctx_err_msg)
RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request.  Consult the documentation on testing for
information about how to avoid this problem.
```
So, I need a request object to use a session object.   Wel, we'll forget about that for now.

I can see how to write tests with assertions to test at least some of my code, but I need to understand how to modularise the testing...

Listening again to Matt Rudge's lectures...

It appears that the approach recommended is to import the test file into the main Python app and add calls to the test functions directly for testing purposes.   This does not seem ideal to me but I will go with it for now.





