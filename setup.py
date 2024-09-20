from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    #this funtion will return the list of requirements

    requirements=[]
    with open(file_path) as fo:
        requirements = fo.readlines()
        requirements = [req.replace("\n", "")for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name = 'mlproject',
    version = '0.0.1',
    author='Gopikrishna',
    author_email='gopikrishnayadam@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)