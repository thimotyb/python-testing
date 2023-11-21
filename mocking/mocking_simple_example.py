# https://docs.python.org/3/library/unittest.mock-examples.html

from unittest.mock import MagicMock

class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass
    def closer(self, something):
        something.close()

# Direct Method Patching
real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3) # This assertion passes
real.method() # Call again
real.something.assert_called_once_with(1, 2, 3) # This assertion fails as method is called twice

# Mock for Method Calls on an Object
mock = Mock()
real.closer(mock)
# this mocks something and calls close via closer, therefore assert passes. 
# The close method on mock (as something) is lazily created at first invocation
mock.close.assert_called_with() 

# Mocking classes:
# we have a function some_function that instantiates Foo and calls a method on it. 
# The call to patch() replaces the class Foo with a mock.
# The Foo instance is the result of calling the mock, so it is configured by modifying the mock return_value.
def some_function():
    instance = module.Foo()
    return instance.method()

with patch('module.Foo') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    assert result == 'the result'