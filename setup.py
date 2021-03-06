#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import autopep8

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass


with open('README.rst') as readme:
    setup(
        name='autopep8',
        version=autopep8.__version__,
        description="A tool that automatically formats Python code to conform to "
                    "the PEP 8 style guide",
        long_description=readme.read(),
        license='Expat License',
        author='Hideo Hattori',
        author_email='hhatto.jp@gmail.com',
        url='https://github.com/hhatto/autopep8',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Programming Language :: Unix Shell',
        ],
        keywords="automation pep8",
        install_requires=['pep8'],
        tests_require=['nose'],
        test_suite='nose.collector',
        py_modules=['autopep8'],
        zip_safe=False,
        entry_points={'console_scripts': ['autopep8 = autopep8:main']},
    )
