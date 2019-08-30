# Windows Projected File System for Python

# What does this project do?

In a nutshell, this allows one to use the Windows Projected File System (ProjFS) API from Python.

This is achieved using ctypes to call library exports in `C:\Windows\System32\ProjectedFSLib.dll`. The function prototypes, enumerations, and defines were manually translated from the Windows SDK header file `<projectedfslib.h>`.

If you're not sure what the Windows Projected File System is, more info can be found at:

* [MSDN docs](https://docs.microsoft.com/en-us/windows/win32/projfs/projected-file-system)
* [Windows Classic Samples](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/ProjectedFileSystem)
* [ProjFS-Managed-API on GitHub](https://github.com/microsoft/ProjFS-Managed-API)

# Project Status

It works on my machine. Making it public in case it helps others.

# How do I get started?

Take a look at [example.py](./example.py) to see how to get started.

# Where can I get more help, if I need it?

Chances are Google will be your friend. Otherwise please feel free to create a GitHub issue.