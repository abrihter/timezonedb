# -*- coding: utf-8 -*-

import setuptools

with open('README.md', 'r',) as f:
    readme = f.read()

setuptools.setup(
    name = 'timezonedb',
    packages = ['timezonedb'],
    version = '0.1',
    description = 'timezonedb.com API [python wrapper]',
    long_description_content_type="text/markdown",
    long_description=readme,
    author = 'bojan',
    author_email = '',
    license='MIT',
    url = 'https://github.com/abrihter/timezonedb/releases',
    download_url = 'https://github.com/abrihter/timezonedb/archive/v_01.tar.gz',
    keywords = ['TIMEZONEDB', 'API', 'WRAPPER'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
