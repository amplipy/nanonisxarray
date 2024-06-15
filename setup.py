from setuptools import setup, find_packages

setup(
    name='nanonisxarray',
    version='0.1',
    author='Petro Maksymovych',
    author_email='pmax20@gmail.com',
    maintainer='Petro Maksymovych',
    maintainer_email='pmax20@gmail.com',
    packages=find_packages(),
    description='compact library to transform .sxm, .3ds and .dat files into xarray',
    long_description=open('README.md').read(),
    install_requires=['tqdm','python-pptx','pyperclip','matplotlib-scalebar','xarray'],
    url='https://github.com/amplifilo/nanonisxarray',
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
