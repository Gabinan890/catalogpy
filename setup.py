from setuptools import setup, find_packages

setup(
    name='catalogpy',
    version='1.5.2',
    description='Libreria per ordinare testi stringhe e liste',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Gabriele Della Fazia Ristori',
    author_email='ristori.dev@gmail.com',
    url='https://github.com/Gabinan890/catalogpy',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
