from setuptools import setup

setup(
    name='Summarizer',
    version='0.1.0',
    description='A program to summarize text, I guess.',
    url='https://gitlab.cl.uni-heidelberg.de/prog1-ws21/prog1-ws21-summarizer6/',
    author='Haigruppe',
    license='GPLv3+',
    packages=['summarizer','summarizer.ui'],
    package_dir={'summarizer': 'src'},
    install_requires=['pycairo',
                      'PyGObject',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Environment :: X11 Applications :: GTK',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'summarizer-cli=summarizer:main'
        ],
        'gui_scripts': [
            'summarizer-ui=summarizer.ui:main'
        ]
    }
)
