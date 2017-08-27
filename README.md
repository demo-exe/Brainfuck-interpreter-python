# Brainfuck-interpreter-python
Yet another brainfuck implementation.

## Getting started

### Prerequisites
You will need [Python 3](https://www.python.org/) to run this program.

### Installation
Clone the project to your workspace
```
git clone git@github.com:demozylak/Brainfuck-interpreter-python.git
```
### Usage
All functionality is embedded in bf.py file.

*Below examples assume that you have your python configured in a way that doesn't require prefixing programs with 'python'
For more informations check [here](https://stackoverflow.com/questions/11472843/set-up-python-on-windows-to-not-type-python-in-cmd)* 

To run helloworld.b type:
```
bf.py helloworld.b
```

You can access help with
```
bf.py --help
```

## Features
Here is a list of supported and planned features
- [x] Full brainfuck syntax
- [x] Nested loops
- [ ] '#' debug command
- [x] Comments in source
- [ ] Command line source input
- [ ] Program blocking user input
- [ ] Output to file
- [ ] Command line parameters for memory size, wrapping, EOF behaviour
- [ ] Error handling