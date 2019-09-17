import unittest

import tests.test_Regex
import tests.test_Helper_Range
import tests.test_Set
import tests.test_Anchor


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(tests.test_Regex))
    suite.addTests(loader.loadTestsFromModule(tests.test_Helper_Range))
    suite.addTests(loader.loadTestsFromModule(tests.test_Set))
    suite.addTests(loader.loadTestsFromModule(tests.test_Anchor))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())