def f(object):
	return 0

def test_equal(actual, expected):
	assert expected  == actual, f'Expected {expected}, actual value returned was {actual}.'

test_equal(f(0),0)