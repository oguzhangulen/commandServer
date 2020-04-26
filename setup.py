from setuptools import setup

setup(
    name='commandServer',
    version='0.1.0',
    packages=['commandsw'],
    entry_points={
        'console_scripts': [
            'commandsw = commandsw.__main__:main'
        ]
    })
