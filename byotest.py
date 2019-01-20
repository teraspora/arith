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

# test_equal(f(0),0)	# should pass

# # test_equal(f(1),1)	# should fail

# test_is_in(7, arr)	# should pass

# # test_is_in(256, arr)	# should fail

# x = 0
# test_exists_as_session_object(x) # should fail

# session["x"] = 0

# test_exists_as_session_object(x) # should pass

# # 3 tests should fail out of 7