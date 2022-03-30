#!/usr/bin/env python3

from setuptools import setup
from DistUtilsExtra.command import (build_i18n, clean_i18n, build_extra, build_icons)

data_files = [
    ('share/applications', ['data/de.haigruppe.summarizer.desktop']),
    ('share/summarizer/data/resources/ui', ['data/resources/ui/shortcuts.ui']),
    ('share/metainfo', ['data/de.haigruppe.summarizer.metainfo.xml']),
]


setup(
    name='Summarizer',
    version='0.1.0',
    description='A program to summarize text, I guess.',
    url='https://gitlab.cl.uni-heidelberg.de/prog1-ws21/prog1-ws21-summarizer6/',
    author='Haigruppe',
    license='GPLv3+',
    packages=['summarizer'],
    package_dir={'summarizer': 'src'},
    data_files=data_files,
    install_requires=['pycairo',
                      'PyGObject',
                      ],
    entry_points={
        'console_scripts': [
            'summarizer-cli=summarizer:main'
        ],
        'gui_scripts': [
            'summarizer-ui=summarizer.ui:main'
            'de.haigruppe.summarizer=summarizer.ui:main'
        ]
    }
)

