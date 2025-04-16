import unittest
import sys

sys.path.append('../')
from xc_fhirpp_sdk.xc_fhirpp_client import XCFHIRPPClient

class TestXCFHIRppClient(unittest.TestCase):
    """Test cases for TestXCFHIRppClient"""

    def test_initialization(self):
        client = XCFHIRPPClient()
        self.assertEqual(client.source_id, 'abc123')

if __name__ == '__main__':
    unittest.main()