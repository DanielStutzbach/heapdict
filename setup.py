#!/usr/bin/env

import sys
if sys.version_info[0] <= 2:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension
else:
    from distutils.core import setup, Extension

setup(name='HeapDict',
      version='0.1.5',
      description='a heap with decrease-key and increase-key operations',
      author='Stutzbach Enterprises, LLC',
      author_email='daniel@stutzbachenterprises.com',
      url='http://stutzbachenterprises.com/',
      license = "BSD",
      keywords = "heap decrease-key increase-key dictionary Dijkstra A*",
      provides = ['heapdict'],
      py_modules = ['heapdict'],
      test_suite = "test_heap",
      zip_safe = True,
      classifiers = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            ],

      long_description="""
HeapDict: a heap with decreased-key and increase-key operations
===============================================================

HeapDict implements the MutableMapping ABC, meaning it works pretty
much like a regular Python dict.  It's designed to be used as a
priority queue, where items are added and consumed as follows:

.. parsed-literal::

    hd = HeapDict()
    hd[obj1] = priority1
    hd[obj2] = priority2
    # ...
    obj = hd.pop()

Compared to an ordinary dict, a HeapDict has the following differences:

popitem():
    Remove and return the (key, priority) pair with the lowest
    priority, instead of a random object.

peekitem():
    Return the (key, priority) pair with the lowest priority, without
    removing it.

Unlike the Python standard library's heapq module, the HeapDict
supports efficiently changing the priority of an existing object
(often called "decrease-key" in textbooks).  Altering the priority is
important for many algorithms such as Dijkstra's Algorithm and A*.
""",
            
      )
