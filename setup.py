import setuptools
import os

with open("README.md", "r") as r:
    ext_desc = r.read()
    
with open("req.txt", "r") as r:
    req = r.read().splitlines()

base_url = "https://github.com/VoxelPrismatic/prizmatic"
setuptools.setup(
    #Info
    name = "prizmatic",
    version = "0.1.3.6",
    author = "PRIZ ;]",
    python_requires = ">=3.6",
    
    #URLs
    url = base_url,
    project_urls = {
        "Issue tracker": base_url+"/issues",
        "Source Code": base_url
    },
    
    #Description
    description = "An API Wrapper for Reddit, Discord, and Matrix [seperate modules, one repo]",
    long_description = ext_desc,
    long_description_content_type = "text/markdown",
    
    #Packages
    packages = [
        'discord'
    ],
    install_requires = req,
    
    #Metadata
    license = "Don't call it your own",
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
    ]
)
