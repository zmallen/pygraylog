#!/usr/bin/env python

from distutils.core import setup

setup(name='pygraylog',
      version='0.3.1',
      description='Graylog API wrapper for python',
      author='Zack Allen',
      author_email='zma4580@gmail.com',
      url='https://www.github.com/zmallen/pygraylog',
      download_url='https://github.com/zmallen/pygraylog/tarball/0.3.1',
      packages=['pygraylog'],
      keywords=['graylog', 'graylog-api', 'api graylog'],
      install_requires=[
          'requests'
      ],
     )
