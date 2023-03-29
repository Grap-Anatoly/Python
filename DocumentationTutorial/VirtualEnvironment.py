# Python applications will often use packages and modules that don’t come as part of the standard library.
# Applications will sometimes need a specific version of a library,
# because the application may require that a particular bug has been fixed or
# the application may be written using an obsolete version of the library’s interface.

# This means it may not be possible for one Python installation to meet the requirements of every application.
# If application A needs version 1.0 of a particular module but application B needs version 2.0,
# then the requirements are in conflict
# and installing either version 1.0 or 2.0 will leave one application unable to run.

# The solution for this problem is to create a virtual environment,
# a self-contained directory tree that contains a Python installation for a particular version of Python,
# plus a number of additional packages.

# Different applications can then use different virtual environments.
# To resolve the earlier example of conflicting requirements, application
# A can have its own virtual environment with version 1.0 installed while application
# B has another virtual environment with version 2.0.
# If application B requires a library be upgraded to version 3.0,
# this will not affect application A’s environment.

# Creating Virtual Environments ---------------------------------------------------------------------

# The module used to create and manage virtual environments is called venv.
# venv will usually install the most recent version of Python that you have available.
# If you have multiple versions of Python on your system,
# you can select a specific Python version by running python3 or whichever version you want.

# To create a virtual environment, decide upon a directory where you want to place it,
# and run the venv module as a script with the directory path:

# python3 -m venv tutorial-env

# Once you’ve created a virtual environment, you may activate it.

# On Windows, run:

# tutorial-env\Scripts\activate.bat

# Managing Packages with pip ---------------------------------------------------------------------------

# You can install, upgrade, and remove packages using a program called pip.
# By default pip will install packages from the Python Package Index,
# <https://pypi.org>. You can browse the Python Package Index by going to it in your web browser.

# pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc.
# (Consult the Installing Python Modules guide for complete documentation for pip.)

# You can install the latest version of a package by specifying a package’s name:

# (tutorial-env) $ pip install novas
# Collecting novas
#   Downloading novas-3.1.1.3.tar.gz (136kB)
# Installing collected packages: novas
#   Running setup.py install for novas
# Successfully installed novas-3.1.1.3

# You can also install a specific version of a package by giving the package name followed by == and the version number:

# (tutorial-env) $ pip install requests==2.6.0
# Collecting requests==2.6.0
#   Using cached requests-2.6.0-py2.py3-none-any.whl
# Installing collected packages: requests
# Successfully installed requests-2.6.0