from setuptools import find_packages, setup


def get_requirements(file_path: str):
    ''' this fn will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

        return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Himanshu Ranjan',
    author_email='20ec3021@rgipt.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)