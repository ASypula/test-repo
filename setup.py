from setuptools import setup, find_packages
  
setup( 
    name='test_module', 
    version='1.0', 
    description='A test Python package', 
    packages=find_packages(include=['test_module']), 
    install_requires=[], 
) 