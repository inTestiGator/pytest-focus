# pytest-focus

Welcome to pytest-focus, a pytest plugin designed to make you focus as you write
test cases until they pass.

# Script Initialization

In order to initialize the shell script that restricts the terminal, you may
need to make the script executable. Use the following commands from the root
directory:

```
cd scripts
chmod +x ptfocus
```

To make this command run for the user-only, an alternative to the `chmod`
command listed above is:

```
chmod u+x ptfocus
```
After the script is made executable, it can be executed from the `scripts/`
directory with the following command:

```
./ptfocus
```
