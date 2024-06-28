from setuptools import setup, find_packages

setup(
    name="mycli",
    version="0.1.0",
    author="Anil Kumar",
    author_email="anil.kumar13@tcs.com",
    description="A CLI tool convert logfiles to json",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/wolwo619/mycli",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mycli=mycli.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here
    ],
)
