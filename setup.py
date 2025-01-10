from setuptools import setup, find_packages

setup(
    name="heehee",
    version="0.1.0",
    author="Runchu Tian",
    author_email="runchutian@gmail.com",
    description="Runchu's personal research toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rachum-thu/heehee",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
    ],
)
