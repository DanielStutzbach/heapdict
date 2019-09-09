#!/usr/bin/env

from setuptools import setup

setup(name='HeapDict',
      version='1.0.1',
      description='a heap with decrease-key and increase-key operations',
      author='Stutzbach Enterprises, LLC',
      author_email='daniel@stutzbachenterprises.com',
      url='http://stutzbachenterprises.com/',
      license = "BSD",
      keywords = "heap decrease-key increase-key dictionary Dijkstra A* priority queue",
      provides = ['heapdict'],
      py_modules = ['heapdict'],
      test_suite = "test_heap",
      zip_safe = True,
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          ],

      long_description=open('README.rst').read(),
      )
