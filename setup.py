#!/usr/bin/env

import sys
if sys.version_info[0] <= 2:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension
else:
    from distutils.core import setup, Extension

setup(name='heapdict',
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

      long_description=open('README.rst').read(),
            
      )
