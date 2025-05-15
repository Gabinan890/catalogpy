from setuptools import setup, find_packages

setup(
    name='catalogpy',
    version='1.2',
    description='Libreria per ordinare testi stringhe e liste',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Gabriele Della Fazia Ristori',
    author_email='gabriele.ristori.0110@gmail.com',
    url='https://github.com/Gabinan890/catalogpy',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)