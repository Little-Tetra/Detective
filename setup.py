from setuptools import setup, find_packages

setup(
    name='Detective',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Little-Tetra/Detective',
    license='MIT',
    author='KevinJu',
    description='A STIX2 GUI editor.',
    install_requires=[
        "stix2",
        "PySide2"
    ],
    package_data={
        'detective': ["resources/*"]
    },
    entry_points={
        'console_scripts': [
            "detective = detective.entries.cli:run"
        ]
    }

)
