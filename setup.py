from setuptools import setup
    
setup(
    name='CSV parser run',
    version='0.1',
    py_modules=['csv_parser_run'],
    install_requires=['Click','pandas'],
    entry_points='''
        [console_scripts]
        csv_parser=csv_parser_run:cli
    ''',
)
