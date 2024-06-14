from setuptools import setup, find_packages

setup(
    name='nanonisxarray',
    version='0.1',
    packages=find_packages(),
    description='compact library to transform .sxm, .3ds and .dat files into xarray, \
                enabling rapid import of experimental data from Nanonis and Tramea controllers into python workspaces.',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().splitlines(),
    url='https://github.com/amplifilo/nanonisxarray',
    author='Petro Maksymovych',
    author_email='5nm@ornl.gov',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)