from setuptools import setup, find_packages

version = '0.1a2.dev0'

setup(
    name='koppeltaal_schema',
    version=version,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        ])
