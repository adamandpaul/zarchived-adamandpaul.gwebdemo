
from setuptools import setup, find_packages
import os

requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'pyramid',
    'pyramid_chameleon',
    'pyramid_zcml',
    'pyramid_debugtoolbar',
    'num2words'
]

setup(

    # Meta Data
    name='adamandpaul.gwebdemo',
    version='1.0',
    description='Google App Engine Buildout Demo',
    login_description='Google App Engine Buildout Demo',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Education',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        ],
    keywords='google app engine buildout demo',
    author='Adam Terrey',
    author_email='software@adamandpaul.biz',
    url='http://adamandpaul.biz',
    license='gpl',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    install_requires=requires,
    test_require=requires,

    entry_points={
        'console_scripts': [
            'gwebdemo_do_nothing=__builtin__:int'
        ],
        'paste.app_factory': [
            'main=adamandpaul.gwebdemo.main:app_factory'
        ],

    },

    test_suite="adamandpaul.gwebdemo",

    )

