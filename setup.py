from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    return  requirements_list

setup(
    name="AI Study Assistant",
    version="0.0.1",
    author="Shravan Kumar Pandey",
    author_email="shravankumarpandey825412@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)