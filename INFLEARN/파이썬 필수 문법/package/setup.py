from setuptools import setup, find_packages

setup(
    name                = 'mypackage_hjp',
    version             = '1.0.0',
    description         = 'package make test',
    author              = 'hojp7874',
    author_email        = 'hojp7874@gmail.com',
    url                 = 'https://github.com/hojp7874',
    download_url        = '',
    install_requires    = [
        'a',
        'b',
        'c'
    ],
    include_package_data= 'True',
    package             = find_packages(),
    keywords            = [],
    python_reuqires     = '>=3',
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ], # https://pypi.org/classifiers/
)