
from setuptools import setup, find_packages
import os

setup(

    # Meta Data
    name='gaebuildoutdemo.app',
    version='1.0'
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
    autoher_email='software@adamandpaul.biz',
    url='http://adamandpaul.biz',
    license='gpl',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-


    ],

    entry_points={
        'console_scripts': [
            'gaebuildoutdemo_app_do_nothing=gaebuildoutdemo.app.do_nothing:run'
        ]

    },
    )

