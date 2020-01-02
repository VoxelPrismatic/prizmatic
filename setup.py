import setuptools
import os

with open("README.md", "r") as r:
    ext_desc = r.read()

with open("req.txt", "r") as r:
    req = r.read().splitlines()

with open("./discord/ver.py") as r:
    ver = r.read().splitlines()[0].split('"')[1]

base_url = "https://github.com/VoxelPrismatic/prizmatic"
docs_site = "https://voxelprismatic.github.io/prizmatic.docs"

setuptools.setup(
    #Info
    name = "prizmatic",
    version = ver,
    author = "PRIZ ;]",
    python_requires = ">=3.6",

    #URLs
    url = base_url,
    project_urls = {
        "Issue tracker": base_url + "/issues",
        "Source Code": base_url,
        "Documentation": docs_site
    },


    #Packages
    packages = [
        'discord'
    ],
    install_requires = req,

    #Metadata
    keywords = "discord reddit matrix riot",
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: None",
        "Operating System :: OS Dependent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],

    #Description
    long_description = ext_desc,
    long_description_content_type = "text/markdown",
    description = "An API Wrapper for Reddit, Discord, and Matrix"
                  "[seperate modules, one repo]"
)
