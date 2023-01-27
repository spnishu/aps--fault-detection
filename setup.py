from setuptools import find_packages,setup

from typing import List

# I want to read my requirement.txt file and return list of string
REQUIREMENT_FILE_NAME="requirements.txt" #Store text file in in variable
HYPHEN_E_DOT = "-e ." #To trigger setup.py file


def get_requirements()->List[str]: #This will return list of string of libraries

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines() #Will read each line

    #replace \n from each line since we are reading text file therefore \n will be there and  \n is not a library
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    #replace -e. since it is not a library it is required to trigger setup file
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.2",
    author="ineuron",
    author_email="avnish@ineuron.ai",
    packages = find_packages(),
    install_requires=get_requirements(),
)