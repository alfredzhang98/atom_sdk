import unittest
from atom_encryption import ErrorDetectionTools

class TestErrorDetectionTools(unittest.TestCase):

    def setUp(self):
        self.data = b"123456789"

    def test_bcc(self):
        # Generate BCC
        bcc = ErrorDetectionTools.BCC.generate(self.data)
        # Verify BCC
        self.assertTrue(ErrorDetectionTools.BCC.verify(self.data, bcc))
        # Test with wrong checksum
        self.assertFalse(ErrorDetectionTools.BCC.verify(self.data, bcc ^ 0xFF))

    def test_crc(self):
        # Test CRC-16-CCITT
        polynomial = 0x1021
        width = 16
        init_value = 0xFFFF
        crc16 = ErrorDetectionTools.CRC.generate(self.data, polynomial, width, init_value)
        # Verify CRC-16
        self.assertTrue(ErrorDetectionTools.CRC.verify(self.data, crc16, polynomial, width, init_value))
        # Test with wrong checksum
        self.assertFalse(ErrorDetectionTools.CRC.verify(self.data, crc16 ^ 0x1, polynomial, width, init_value))

    def test_parity(self):
        # Test even parity
        parity_even = ErrorDetectionTools.Parity.generate(self.data, even_parity=True)
        self.assertTrue(ErrorDetectionTools.Parity.verify(self.data, parity_even, even_parity=True))
        # Test odd parity
        parity_odd = ErrorDetectionTools.Parity.generate(self.data, even_parity=False)
        self.assertTrue(ErrorDetectionTools.Parity.verify(self.data, parity_odd, even_parity=False))
        # Test with incorrect parity bit
        self.assertFalse(ErrorDetectionTools.Parity.verify(self.data, parity_even ^ 0x1, even_parity=True))

    def test_lrc(self):
        # Generate LRC
        lrc = ErrorDetectionTools.LRC.generate(self.data)
        # Verify LRC
        self.assertTrue(ErrorDetectionTools.LRC.verify(self.data, lrc))
        # Test with wrong checksum
        self.assertFalse(ErrorDetectionTools.LRC.verify(self.data, lrc ^ 0xFF))

if __name__ == "__main__":
    unittest.main()
