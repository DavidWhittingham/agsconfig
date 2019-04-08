from setuptools import setup, find_packages

with open('agsconfig/_version.py') as fin: exec(fin.read(), globals())
with open('requirements.txt') as fin: requirements=[s.strip() for s in fin.readlines()]
with open('readme.md') as fin: long_description = fin.read()

packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name = "agsconfig",
    version = __version__,
    packages = packages,

    #dependencies
    install_requires = requirements,

    #misc files to include
    package_data = {
        "": ["LICENSE"]
    },

    #PyPI MetaData
    author = __author__,
    description = "Provides classes that can edit ArcGIS service configuration as either running services (ArcGIS Server Admin JSON format) or Service Definition Drafts.",
    long_description = long_description,
    license = "BSD 3-Clause",
    keywords = "arcgis esri",
    url = "https://github.com/DavidWhittingham/agsconfig",
    classifiers = (
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6"
    ),

    zip_safe = False
)
