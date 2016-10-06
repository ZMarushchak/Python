import unittest
from subprocess import check_output
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class test(unittest.TestCase):

    def test(self):
        #print "CURRENT DIR::::%s" % CURRENT_DIR
        out = check_output(["python", CURRENT_DIR + "/app.py"])
        # print "PRINTED:%s" % out
        return self.assertTrue(out.find('Hello')!=-1)

suite = unittest.TestLoader().loadTestsFromTestCase(test)
runner = unittest.TextTestRunner(verbosity=2).run(suite)
ret = not runner.wasSuccessful()
sys.exit(ret)

