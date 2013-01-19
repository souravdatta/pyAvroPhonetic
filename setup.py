#!/usr/bin/env python

from distutils.core import setup
from pyavrophonetic import __version__

setup(name='PyAvroPhonetic',
      version=__version__,
      description='Python implementation of Avro Phonetic',
      long_description=open('README.rst', 'rt').read(),
      author='Kaustav Das Modak',
      author_email='kaustav.dasmodak@yahoo.co.in',
      url='https://github.com/kaustavdm/pyAvroPhonetic',
      packages=['pyavrophonetic',],
      license='GNU GPL v3 or later',
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        ]
      )