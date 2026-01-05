#numpy 

In python in a long dtype we have four pieces:
- ob_refcnt: reference count that helps python handle memory alloc/dealloc
- ob_type: encodes type of the variable
- ob_size: specifies the size of the following data members
- ob_digit: the actual integer value

Vanilla python list:
Generates a block of pointers that points to a python objects.