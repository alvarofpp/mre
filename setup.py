import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mre',
    version='0.12.0',
    author='Álvaro Ferreira Pires de Paiva',
    author_email='alvarofepipa@gmail.com',
    description='Maker Regular Expressions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alvarofpp/mre',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
