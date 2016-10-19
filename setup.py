from setuptools import setup

setup(
    name='roler',
    version='0.1',
    py_modules=['roler'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        roler=roler:create_role
    ''',
)
