from Core import input, output, source, memory
from Core import interpreter
from Core import version

#argument parsing
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="Commandline Brainfuck interpreter", epilog="https://github.com/demozylak/Brainfuck-interpreter-python", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("file", metavar='FILE', type=argparse.FileType('r'), help="brainfuck source file to be interpreted")
parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=version.__version__))
parser.add_argument('-r', '--read-from', dest='input_file', metavar='INPUT_FILE', type=argparse.FileType('r'), help="input file for brainfuck program") 
parser.add_argument('-i', '--input', dest='input_string', metavar='INPUT', help="input string for brainfuck program") 

args = parser.parse_args()

#Arguments interpreting
#Source
s = source.FileSource(args.file)

#Input
if(args.input_file != None):
    i = input.StringInput(args.input_file.read())
elif(args.input_string != None):
    i = input.StringInput(args.input_string)
else:
    i = input.StdinInput()

#Output
o = output.StdinOutput()

#Memory
m = memory.Memory()

interpreter.Interpreter(s, i, o, m).run()

