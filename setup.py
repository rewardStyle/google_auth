"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='google_auth',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',  # Required

    description='A Python3 library for handling Google authentication for services such as Google Drive and Google Docs',  # Required

    long_description=long_description,  # Optional

    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/rewardStyle/google_auth',  # Optional

    author='rewardStyle DevOps',  # Optional

    author_email='devops@rewardstyle.com',  # Optional

    packages=find_packages(exclude=['Pipfile', 'Pipfile.lock', 'client_secret.json', 'client_credentials.json']),  # Required

    install_requires=['oauth2client'],  # Optional

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/rewardStyle/google_auth/issues',
        'Source': 'https://github.com/rewardStyle/google_auth',
        'Google API Docs': 'https://developers.google.com/sheets/api/quickstart/python',
        'Google Auth Scopes Docs': 'https://developers.google.com/identity/protocols/googlescopes'
    },
)
