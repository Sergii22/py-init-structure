from setuptools import find_packages, setup

requirements = [
    "click==7.1.2",
    "questionary==1.8.0"
]

setup(
    name="py-init-structure",
    packages=find_packages(),
    version="0.1.0",
    description="Creates structure of autotest project",
    author="Sergii Golovach",
    license="MIT",
    install_requires=requirements,
    entry_points='''
            [console_scripts]
            myhello=controller:create_structure
        '''
)