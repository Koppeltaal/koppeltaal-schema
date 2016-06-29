from setuptools import setup, find_packages

version = '0.1a1'

setup(
    name='koppeltaal_schema',
    version=version,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        ])
