from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(File_Path: str)->List[str]:
    '''
    This function will returen the list of reuqiements 
    '''    
    requirement = []
    with open(File_Path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]
        
        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    return requirement

setup(
    name='Data_Preporcessing',
    version='1.1',
    author= 'Vraj Patel',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt') 
    # install_requires=['numpy','pandas','scikit-learn','matplotlib'], -> if you have less packages to install
    
)