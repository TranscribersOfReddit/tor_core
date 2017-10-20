import codecs
import os
import sys

from setuptools import (
    setup,
    find_packages,
)
from setuptools.command.test import test as TestCommand

from tor_core import __version__


class PyTest(TestCommand):
    # From: https://stackoverflow.com/a/43924004/1236035
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def long_description():
    if not (os.path.isfile('README.md') and os.access('README.md', os.R_OK)):
        return ''

    with codecs.open('README.md', encoding='utf8') as f:
        return f.read()


test_deps = [
    'pytest',
    'pytest-cov',
]
dev_helper_deps = [
    'better-exceptions',
]


setup(
    name='tor_core',
    version=__version__,
    description='Core functionality used across /r/TranscribersOfReddit bots',
    long_description=long_description(),
    url='https://github.com/TranscribersOfReddit/tor_core',
    author='Joe Kaufeld',
    author_email='joe.kaufeld@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: Communications :: BBS',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    packages=find_packages(exclude=['test*', 'bin/*']),
    cmdclass={'test': PyTest},
    test_suite='test',
    tests_require=test_deps,
    extras_require={
        'dev': test_deps + dev_helper_deps,
    },
    install_requires=[
        'praw==5.0.1',
        'redis<3.0.0',
        'sh',
        'bugsnag',
        'cherrypy',
        'addict',
        'raven',  # Sentry client
    ],
)
