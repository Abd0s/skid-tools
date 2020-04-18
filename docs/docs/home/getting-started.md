
# Getting started

## Prerequisites

Skidtools works with Python 3.6 or higher. Support for earlier versions of Python is not provided. Python 2.7 or lower is not supported. 

## Installation

While there are several ways of installing Skidtools, the recommended method is by using `pip` - the Python package manager.

### with pip <small>recommended</small>

Skidtools can be installed with `pip`:

``` sh
pip install skidtools
```

!!! tip "Installation in a virtual environment"

    The best way to make sure that you end up with the correct versions and
    without any incompatibility problems between packages it to use a **virtual
    environment**. Don't know what this is or how to set it up? We recommend
    to start by reading a [tutorial on virtual environments][1] for Python.

!!! warning "Installation on macOS"

    When you're running the pre-installed version of Python on macOS, `pip`
    tries to install packages in a folder for which your user might not have
    the adequate permissions. There are two possible solutions for this:

    1. **Installing in user space** (recommended): Provide the `--user` flag
      to the install command and `pip` will install the package in a user-site
      location. This is the recommended way.

    2. **Switching to a homebrewed Python**: Upgrade your Python installation
      to a self-contained solution by installing Python with Homebrew. This
      should eliminate a lot of problems you could be having with `pip`.
    
[1]: https://docs.python-guide.org/dev/virtualenvs/

### with git

Skidtools can be directly installed from [GitHub][2] by cloning the
repository which might be useful if you want to use the very latest version:

``` sh
git clone https://github.com/Abd0s/skidtools/
```

Then just run the setup.py file from that directory.

``` sh
python setup.py install
```

[2]: https://github.com/Abd0s/skidtools/

## Basic Usage

### Initilization

A `config.py` file is required for every application using skidtools, it contains all the configurations options required.
You can make one manually or generate a default one with the builtin ``--init`` command.

``` sh
python -m skidtools --init
```

### Using Modules

Using the IO submodule we can insert colored text into print statements.

``` python
from skidtools import sio

print(f"Hello {sio.colored_print("world", "red")}")

```

We can initialize the logging module with default behavoir and command line options.

``` python
from skidtools import slogging

import logging
import sys

slogging.init_logging(sys.argv)

if 3 + 2 == 5:
  logging.succes("3 + 2 is equal to 5")
else:
  logging.error("3 + 2 is not equal to 5")

logging.debug("done addition")
```

Running this with

``` sh
python example.py
```

Will output:

``` sh
INFO:root:3 + 2 is equal to 5
```

if we run this with the `-d` flag, it will now output the logs on debug level.

``` sh
INFO:root:3 + 2 is equal to 5
DEBUG:root:done addition
```

For further reference: [More about modules](modules.md)

