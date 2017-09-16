import unittest
import os 


def load_tests(loader, standard_tests, pattern):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return unittest.TestLoader().discover(dir_path)

if __name__ == '__main__':
    unittest.main(verbosity = 3)