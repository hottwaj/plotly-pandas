from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='plotly-pandas',

    version='1.3',
    
    python_requires='>3.7',

    description='Basic tools to create plotly charts from pandas DataFrames, using dictionary-based layout specs rather than plotly-python Graph Objects',
    long_description=long_description,

    url='https://github.com/hottwaj/plotly-pandas',

    author='Jonathan Clarke',
    author_email='jonathan.a.clarke@gmail.com',

    license='MIT, Copyright 2021',

    classifiers=[
    ],

    keywords='',

    py_modules=['plotly_pandas'],
    
    install_requires=["plotly>=4.14.0",
                      "numpy",
                      "pandas>=1.2.0",
                      "ipython",
                      "nbformat",],
)

