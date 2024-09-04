# IDAPythonScripts
This repo contains interesting IDAPython scripts for reverse engineering. IDA Pro provides useful API for working with an open IDB database file, including functions for enumerating end editing file data. Unfortunately, IDA Free doesn't have the capability to run Python scripts. IDA comes with a bundled Python interpreter setup, but this version is usually outdated, so it's often necessary to retarget the tool to work with the already installed interpreter. IDA Pro includes a tool to simplify this process, called `idapyswitch.exe`, which is located in the installation directory. `idapyswitch` detects installed Python versions and allows you to select that one you want to use. With this tool, you can easily switch to a different Python version and check which one is currently active. This option is more convenient than manually replacing files in the program's installation directory. 

The output from `idapyswitch` is shown below.

![alt text](https://github.com/user-attachments/assets/00137a2f-75ac-473e-b9f1-9167d4732d9b)
