from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='RequestOn',

    version='0.0.1',

    description='Create and manage apps services requests with python',
    long_description='RequestOn is a python open source software that allow check the '
                     'availability of services. It uses dashy as dashboard '
                     'to show the status of the service.',
    url='https://github.com/nicolastrres/requestOn',
    author='Nicolas Agustin Torres',
    author_email='nicolastrres@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='link checking development dashy requests status_codes',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'tests*']),


    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'requestOn=requestOn.__main__:main',
        ],
    },
)
