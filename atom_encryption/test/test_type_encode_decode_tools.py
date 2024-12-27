import unittest
from atom_encryption import TypeEncodeDecodeTools

class TestTypeEncodeDecodeTools(unittest.TestCase):

    def setUp(self):
        self.tools = TypeEncodeDecodeTools()

    def test_int_list_to_str_and_str_to_int_list(self):
        int_list = [72, 101, 108, 108, 111]
        string = self.tools.int_list_to_str(int_list)
        self.assertEqual(string, "Hello")
        self.assertEqual(self.tools.str_to_int_list(string), int_list)

    def test_int_list_to_tuple_and_tuple_to_int_list(self):
        int_list = [1, 2, 3]
        int_tuple = self.tools.int_list_to_tuple(int_list)
        self.assertEqual(int_tuple, (1, 2, 3))
        self.assertEqual(self.tools.tuple_to_int_list(int_tuple), int_list)

    def test_char_list_to_int_list_and_int_list_to_char_list(self):
        char_list = ['H', 'e', 'l', 'l', 'o']
        int_list = [72, 101, 108, 108, 111]
        self.assertEqual(self.tools.char_list_to_int_list(char_list), int_list)
        self.assertEqual(self.tools.int_list_to_char_list(int_list), char_list)

    def test_char_list_to_str_and_str_to_char_list(self):
        char_list = ['H', 'e', 'l', 'l', 'o']
        string = "Hello"
        self.assertEqual(self.tools.char_list_to_str(char_list), string)
        self.assertEqual(self.tools.str_to_char_list(string), char_list)

    def test_hex_string_to_int_list_and_int_list_to_hex_string(self):
        hex_string = "48656c6c6f"
        int_list = [72, 101, 108, 108, 111]
        self.assertEqual(self.tools.hex_string_to_int_list(hex_string), int_list)
        self.assertEqual(self.tools.int_list_to_hex_string(int_list), hex_string)

    def test_bytes_to_int_list_and_int_list_to_bytes(self):
        byte_data = b"Hello"
        int_list = [72, 101, 108, 108, 111]
        self.assertEqual(self.tools.bytes_to_int_list(byte_data), int_list)
        self.assertEqual(self.tools.int_list_to_bytes(int_list), byte_data)

    def test_float_to_bytes_and_bytes_to_float(self):
        float_value = 12.34
        float_bytes = self.tools.float_to_bytes(float_value)
        self.assertEqual(self.tools.bytes_to_float(float_bytes), float_value)

    def test_bytes_to_hex_string_format_and_hex_string_format_to_bytes(self):
        byte_data = b"Hello"
        formatted_hex = self.tools.bytes_to_hex_string_format(byte_data)
        self.assertEqual(formatted_hex, "\\x48\\x65\\x6c\\x6c\\x6f")
        self.assertEqual(self.tools.hex_string_format_to_bytes(formatted_hex), byte_data)

    def test_int_to_int_list_and_int_list_to_int(self):
        integer_value = 123456
        int_list = self.tools.int_to_int_list(integer_value, specified_length=4, order="msb")
        self.assertEqual(int_list, [0, 1, 226, 64])
        self.assertEqual(self.tools.int_list_to_int(int_list, "msb"), integer_value)

    def test_bin_string_to_int_list_and_int_list_to_bin_string(self):
        binary_string = "0100100001100101011011000110110001101111"
        int_list = [72, 101, 108, 108, 111]
        self.assertEqual(self.tools.bin_string_to_int_list(binary_string), int_list)
        self.assertEqual(self.tools.int_list_to_bin_string(int_list), binary_string)

if __name__ == "__main__":
    unittest.main()
