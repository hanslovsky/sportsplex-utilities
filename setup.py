from setuptools import setup

setup(
    name='sportsplex-utilities',
    version='0.1.0',
    description='Utilities to make life easier for team captains at the sportsplex.',
    packages=['sportsplex'],
    author='Philipp Hanslovsky',
    author_email='philipp.hanslovsky@gmail.com',
    url='https://github.com/hanslovsky/sportsplex-utilities',
    entry_points={
        'console_scripts': [
            'convert-schedule=sportsplex.convert_schedule:main'
        ]
    }
)
