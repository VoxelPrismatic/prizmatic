# PRIZMATIC
An API Wrapper for Reddit, Discord, and Matrix [seperate modules, one repo]

# LICENSE
Ok, so here's the deal, I don't want to get into licensing things because I don't want to
get in trouble. So, here is the *very official* license that I just made up:
```
Feel free to do whatever you want with this software. Just do not pass it off as your own.
It is provided "as-is", and all issues sould be reported to this repository. No warranty
or anything is provided, just this, and my willingness to do stuff.
```
Now that we got that out of the way, info on Discord, Reddit, and Matrix

# THIS WRAPPER
This repository is split into 3 submodules:
```
> "discord" - the Discord bit
> "reddit" -- the Reddit bit
> "riot" ---- the Matrix/Riot bit
```
These modules are seperate, but you can interact with them in mostly
the same way if you like. The biggest difference between any of these
modules are the class names.

# DEPENDENCIES
```
1] py3.5 to py3.7, don't use py3.8 because I can't verify if it works there.
2] Knowledge of code
>  Basically, I will make this module as easy as possible to understand,
>  but you still need to actually make your own code
```
Install the requirements:
```
Windows   ] C:\>py -m pip install -U req.txt
Linux/Mac ] ~$ python -m pip install -U req.txt
```
**This is not a package yet. Do not bug me about that.**

# DOCUMENTATION
I don't know how to document stuff... so the best I can say is just look at the code.

When I do document stuff, it will generally follow this syntax:
```
DESCRIPTION ---
    Description of the class blah represents blah blah

PARAMS ---
    param_name [type]
    - Description of this param
    
    Maybe you shouldn't initialize this class.

FUNCTIONS ---
    await function1(...)
    - Description
    
    function2()
    - Description 2 
```
Please note that classes that shouldn't be initialized will not have their
params shown, as they are formed according to [the discord docs](https://discordapp.com/developers/docs)

Also, all the documentation will be in those files for now. I will provide
further examples and info in the wiki of this repo, but only when this thing
actually starts to work.

# CODE
To see how I name stuff for little bits of code, go to `ParamNames.md`
