# coding: utf-8
from setuptools import setup

"""CLI-template renderer like m4 but based on jinja"""

setup(
    name='jinjarg',
    version='0.0.1',
    url='https://github.com/strizhechenko/jinjarg',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description=__doc__,
    py_modules=['jinjarg'],
    platforms='any',
    install_requires=['jinja2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: CLI',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
