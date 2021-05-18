from setuptools import setup

setup(
    name="resourcemanager",
    version='0.0.1',
    author='Diego',
    description='',
    license='GNU',
    install_requires='flask',
    entry_points={
        'console_scripts': [
            'resourcemanager_docker=resourcemanager:main'
        ]
    }

)