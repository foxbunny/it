==
It
==

Higher order operators for functional programming in Python.

Motivation
==========

When using functional programming techniques in Python, we occasionally run into
code that looks like this::

    filter(lambda x: x < 3, [1, 2, 3, 4, 5])

While ``lambda``s are not exactly complex, it still takes a bit of time for the
reader to parse the lambda and figure out what the intent was.

The ``it`` object makes the code more readable by capturing the intent without
a lot of syntax::

    filter(it < 3, [1, 2, 3, 4, 5])

Implementation
==============

Behind the scenes, the ``it`` object implements `Python's magic methods
<https://docs.python.org/3/reference/datamodel.html#basic-customization>`_, and
returns a function (a lambda, to be exact), that performs the task of the
construct in which ``it`` was used.

Therefore, ``it < 2`` becomes ``lambda x: x < 2``.

Supported constructs
====================

The following constructs are supported:

- comparison operators (e.g., ``it < 2``, ``4 >= it``)
- attribute access (e.g., ``it.foo``)
- subscript access (e.g., ``it['foo']``, ``it[0]``, ``it[-2:]``)
- function calls (e.g., ``it(1, 2)``, ``it(foo='bar')``)
- mathematical operators (e.g., ``it + 2``, ``20 / it``)
- binary operators (e.g., ``it & 4``, ``128 | it``)
- some unary operators (i.e., ``-it``, ``+it``, and ``~it``)

Limitations
===========

Because of the underlying limtiation of the Python language, there are a few
cavats when using ``it``.

Reverse pow
-----------

The reverse ``pow()``, where ``it`` is in the second position, cannot be used
with modulo. For example, ``pow(2, it, 3)`` is cause a ``TypeError``.

No unary assignment operators
-----------------------------

Since unary operators such as ``-=`` do not make much sense for the intended
usage of the ``it`` object, they are not implemented. Use the binary operators
(e.g., ``it - n``) instead.

No setters
----------

There are no aliases for setting attributes and keys. For example, you are not
allowed to say ``map(it.foo = 12, ...)``. It was decided that adding unfamiliar
methods is inferior to simply using lambdas, so support for these constructs was
not added in any form.

No aliases for features having a single-argument magic methods
--------------------------------------------------------------

Where python already supplies adequate functions, the magic methods were
omitted. For example, ``str()``, ``int()``, ``bool()``, ``len()``, etc, should
be used directly. This is also due to the fact that such function have
expectation about return values of the magic methods which cannot be satisfied.

License
=======

This code is published under the BSD license. Please see the ``LICENSE`` file in
the source tree.