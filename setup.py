from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='mode_helper',
    version='0.1',
    author='Pedro Coelho',
    author_email='maia.coelho.dev@gmail.com',
    url='https://github.com/maia-dev/mode_helper',
    description='A visual menu for i3wm modes',
    long_description=readme(),
    license='GPLv3+',
    packages=['mode_helper'],
    include_package_data=True,
    install_requires=[
        'argparse',
        'configparser',
        'gi',
    ],
    entry_points={
        'console_scripts': ['mode_helper=mode_helper.run:main'],
    }
)
