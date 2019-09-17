import unittest

import tests.test_Regex
import tests.test_Helper_Range


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(tests.test_Regex))
    suite.addTests(loader.loadTestsFromModule(tests.test_Helper_Range))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())