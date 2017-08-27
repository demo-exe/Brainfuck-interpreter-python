
from Core import input
from Core import output
from Core import source
from Core import interpreter



interpreter.Interpreter(source.FileSource('helloworld.b'), input.StdinInput(), output.StdinOutput()).run()

