from Core import input, output, source, memory
from Core import interpreter
from Core import version

#argument parsing
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="Commandline Brainfuck interpreter\nhttps://github.com/demozylak/Brainfuck-interpreter-python", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("input_file", type=str, help="source file to be interpreted")
parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=version.__version__))

args = parser.parse_args()


s = source.FileSource(args.input_file)
i = input.StdinInput()
o = output.StdinOutput()
m = memory.Memory()

interpreter.Interpreter(s, i, o, m).run()

