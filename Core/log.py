import logging

logger = logging.getLogger('BrainfuckPythonInterpreter')

_sh = logging.StreamHandler()
_formatter = logging.Formatter('[%(levelname)s] <%(filename)17s @%(lineno)4s> - %(funcName)17s(): %(message)s')
_sh.setFormatter(_formatter)
logger.addHandler(_sh)

def LogSetLevel(lvl):
    logger.setLevel(lvl)

