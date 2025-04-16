from setuptools import setup, find_packages

def load_requirements(filename='requirements.txt'):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"Warning: {filename} not found, no dependencies loaded.")
        return []

setup(
    name='xc_fhirpp_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=load_requirements(),
    author='Chris DiMaio',
    description='A thin wrapper for XCaliber Health\'s FHIR',
    python_requires='>=3.9'
)