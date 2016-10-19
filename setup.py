from setuptools import setup

setup(
    name='roler',
    version='0.1',
    description='A simple tool that creates an ansible role \
                 with the reccomended directory layout',
    author='Nikola Divic',
    author_email='divicnikola@gmail.com',
    url='https://github.com/TheDivic/roler',
    download_url='https://github.com/TheDivic/roler/tarball/0.1',
    keywords=['ansible', 'role'],
    py_modules=['roler'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        roler=roler:create_role
    ''',
)
