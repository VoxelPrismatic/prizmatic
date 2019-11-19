import setuptools

with open("README.md", "r") as readme:
    ext_desc = readme.read()
    
with open("req.txt", "r") as r:
    req = r.read().splitlines()

setuptools.setup(
    name = "prizmatic",
    version = "0.1.3.6",
    author = "PRIZ ;]",
    project_urls={
        "Issue tracker": "https://github.com/VoxelPrismatic/prizmatic/issues",
    },
    description = "An API Wrapper for Reddit, Discord, and Matrix [seperate modules, one repo]",
    long_description = ext_desc,
    long_description_content_type = "text/markdown",
    url = "https://github.com/VoxelPrismatic/prizmatic",
    packages = ['discord'],
    install_requires = req,
    license = "Don't call it your own",
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: None",
        "Operating System :: OS Dependent",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires = '>=3.6'
)
