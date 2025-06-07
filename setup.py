from setuptools import setup, find_packages

setup(
    name="jm_utils",
    version="0.1.0",
    author="Jorge Monti",
    author_email="jorgitomonti@gmail.com",
    description="Utilities i use frecuntly",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jmonti-gh/Ideas",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "rich",
        "wmi"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
