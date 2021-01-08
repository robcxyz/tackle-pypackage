#!/usr/bin/env python

"""The setup script."""
import codecs
import os

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'rich>=3.3.0',
    'pydantic>=1.6.0',
    'PyYAML>=5.3.0'
    'typer>=0.3.2'
]


def _read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    """Get the version from the __init__ file in the app dir."""
    for line in _read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    version=get_version(os.path.join('app', '__init__.py')),
    author="{{name}}",
    author_email='{{email}}',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="{{project_short_description}}",
    entry_points={
        'console_scripts': [
            '{{project_slug}}=app.main:main',
        ],
    },
    install_requires=requirements,
    # license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{project_slug}}',
    name='{{project_slug}}',
    packages=find_packages(include=['app', 'app.*']),
    test_suite='tests',
    url='https://github.com/{{github_username}}/{{project_slug}}',
    zip_safe=False,
)
