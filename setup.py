from setuptools import setup

with open("./README.md", "r") as arq:
    readme = arq.read()

setup(name='JSON Checker',
    version='1.0',
    license='MIT License',
    author='Alan Reis Anjos',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='alanreisanjo@gmail.com',
    keywords='JSON Checker',
    description=u'Pequena biblioteca para verificar se um arquivo JSON está de acordo com um schema',
    packages=['jsonChecker'])