# Xent-cli

The official CLI and interpreter for the Xentext langauge.

------------------------------

# to download:

Download as a ZIP or clone this repository to use, you must have python3 and the argparse module (in the standard library)

this comes with the python edition of XenText

------------------------------

# command line flags

Xent comes with a selection of command line flags. You execute them with the start command-

```python
python3 main.py <flags>
```

`-h` - view help text<br>
`--version` - view CLI version<br>
`-r <scriptname/path>` - run a .xt file through the lexer<br>

if you want to enter the interpreter, just run 
```python
python3 main.py
```

-------------------------------

# interpreter commands

Type any Xent code into the interpreter and it will save to a file, this file is deleted later on.

1. `run()` - run any code you typed in earlier
2. `forcerun()`- run any code WITHOUT UNLINKING THE FILE
3. `exit()` - exit the interpreter/unlink all session files
4. `moomoo()` - :D we brought a cow!

---------------------------------

# configuration file

Xent reads CLI configuration from **config.py**, which must exist for the CLI to run. You can use the 
following sample to save hassle:

```python
PARSER_LOCATION = "xent.py " # Add a space after the name or you'll have issues
DISABLE_SCRIPT_EXECUTION = "false" # Stop Xent from executing your scripts and run code only from the interpreter
INSTALLED_PACKAGES = [] # packages ( quick complex, leave it to the experts!)
```

---------------------------------

# quite obvious small print

> &copy; 2020 17lwinn/XentDevs
> &copy; 2020 Jonyk56 ( Creator )