import logging

logger = logging.getLogger('BrainfuckPythonInterpreter')

_sh = logging.StreamHandler()
_formatter = logging.Formatter('[%(levelname)s] <%(filename)s@%(lineno)s> - %(funcName)20s(): %(message)s')
_sh.setFormatter(_formatter)
logger.addHandler(_sh)

def LogSetLevel(lvl):
    logger.setLevel(lvl)

