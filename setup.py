from setuptools import setup

cfg = {
    "name": 'packaging_with_mypy_b',
    "version": '0.0.1',
    "url": 'https://github.com/austinjp/packaging-with-mypy-b',
    "author": 'austinjp',
    "packages": ["packaging_with_mypy_b"],
    "package_data": {
        "gunicorn":["stubs/gunicorn"],
    },
    "install_requires": [
        'gunicorn @ https://pypi.org/project/gunicornxxx/',
    ]
}

setup(**cfg)
