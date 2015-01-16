try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Create and manage apps services requests with python',
    'author': 'Nicolas Agustin Torres',
    'license': 'MIT License',
    'url': 'https://github.com/nicolastrres/checkit/',
    'download_url': 'Where to download it.',
    'author_email': 'nicolastrres@gmail.com',
    'version': '0.1',
    'install_requires': 'requirements',
    # 'packages': ['NAME'],
    # 'scripts': [],
    'name': 'CHECKIT'
}

setup(**config)