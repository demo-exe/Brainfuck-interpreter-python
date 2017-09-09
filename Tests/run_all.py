import unittest

def load_tests(loader, standard_tests, pattern):
    return unittest.TestLoader().discover('.')

if __name__ == '__main__':
    unittest.main(verbosity = 3)