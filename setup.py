from setuptools import setup

# Kudos: https://blog.ian.stapletoncordas.co/2019/02/distributing-python-libraries-with-type-annotations.html

cfg = {
    "name": 'packaging_with_mypy_b',
    "version": '0.0.1',
    "url": 'https://github.com/austinjp/packaging-with-mypy-b',
    "author": 'austinjp',
    "packages": [
        "packaging_with_mypy_b"
    ],
    "package_data": {
        "packaging_with_mypy_b": [
            "*.pyi",
            "**/*.pyi",
            "py.typed"
        ],
        "gunicorn": [
            "stubs/gunicorn"
        ],
    },
    "include_package_data": True,
    "install_requires": [
        'gunicorn',
    ]
}

setup(**cfg)
