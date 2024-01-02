from setuptools import setup

with open("./README.md", "r") as arq:
    readme = arq.read()

setup(name='JSON Manager',
    version='1.0',
    license='MIT License',
    author='Alan Reis Anjos',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='alanreisanjo@gmail.com',
    keywords='JSON Manager',
    description=u'Pequena biblioteca para validação e manipulação de JSONs;',
    packages=['jsonManager'])