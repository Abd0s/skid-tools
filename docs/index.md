# What is skidtools?

Skidtools is a collection of utilities designed to speed up prototyping and scripting. 
It replaces common boilerplate code such as loading an `username:email` formatted file, or setting up logging. It does this all very opinionated, but consistent. 
This allows people to test concepts very rapidly without sacrificing features, code integrity and safety.

## For who skidtools is

You are looking to quickly try out an idea, make a script for personal use and you don't require much custumization.
For example, you want to know how many combos you have.

``` python
from skidtools import slogging, sio
import sys
import logging

slogging.init_logging(sys.argv)
combos = sio.load_combos()

# Do something with combos
logging.info(f"{len(combos)} combos loaded")
```


## For who skidtools is **NOT**

You are looking to make a full fledge application with proper configurability. While skidtools could work for you, it's not recommended. You will likely need a level of control which skidtools doesn't provide. Eg. you want to use your own formatting for logging and outputs in general.
