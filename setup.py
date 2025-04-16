from setuptools import setup, find_packages

setup(
    name='fhir_plusplus_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Chris DiMaio',
    description='A thin wrapper for XCaliber Health\'s FHIR',
    python_requires='>=3.9'
)