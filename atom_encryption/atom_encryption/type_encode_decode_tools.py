import sys
from typing import List, Tuple, Literal
import struct

class TypeEncodeDecodeTools:
    # Integer List to String
    @staticmethod
    def int_list_to_str(int_list: List[int]) -> str:
        """Convert a list of integers to a string, interpreting each integer as an ASCII character.
        Example:
            Input: [65, 66, 67]
            Output: 'ABC'
        """
        return ''.join(chr(i) for i in int_list)

    # String to Integer List
    @staticmethod
    def str_to_int_list(string: str) -> List[int]:
        """Convert a string to a list of integers, where each integer represents an ASCII character code.
        Example:
            Input: 'Hello'
            Output: [72, 101, 108, 108, 111]
        """
        return [ord(c) for c in string]

    # Integer List to Tuple
    @staticmethod
    def int_list_to_tuple(int_list: List[int]) -> Tuple:
        """Convert a list of integers to a tuple.
        Example:
            Input: [1, 2, 3]
            Output: (1, 2, 3)
        """
        return tuple(int_list)

    # Tuple to Integer List
    @staticmethod
    def tuple_to_int_list(u_tuple: Tuple) -> List[int]:
        """Convert a tuple to a list of integers.
        Example:
            Input: (1, 2, 3)
            Output: [1, 2, 3]
        """
        return list(u_tuple)

    # Character List to Integer List
    @staticmethod
    def char_list_to_int_list(char_list: List[str]) -> List[int]:
        """Convert a list of characters to a list of integers (ASCII codes).
        Example:
            Input: ['H', 'e', 'l', 'l', 'o']
            Output: [72, 101, 108, 108, 111]
        """
        return [ord(c) for c in char_list]

    # Integer List to Character List
    @staticmethod
    def int_list_to_char_list(int_list: List[int]) -> List[str]:
        """Convert a list of integers to a list of characters, interpreting each integer as an ASCII character.
        Example:
            Input: [72, 101, 108, 108, 111]
            Output: ['H', 'e', 'l', 'l', 'o']
        """
        return [chr(i) for i in int_list]

    # Character List to String
    @staticmethod
    def char_list_to_str(char_list: List[str]) -> str:
        """Convert a list of characters to a string.
        Example:
            Input: ['H', 'e', 'l', 'l', 'o']
            Output: 'Hello'
        """
        return ''.join(char_list)

    # String to Character List
    @staticmethod
    def str_to_char_list(string: str) -> List[str]:
        """Convert a string to a list of characters.
        Example:
            Input: 'Hello'
            Output: ['H', 'e', 'l', 'l', 'o']
        """
        return list(string)

    # Hex String to Integer List
    @staticmethod
    def hex_string_to_int_list(hex_string: str) -> List[int]:
        """Convert a hex string to a list of integers.
        Example:
            Input: '48656c6c6f'
            Output: [72, 101, 108, 108, 111]
        """
        return [int(hex_string[i:i + 2], 16) for i in range(0, len(hex_string), 2)]

    # Integer List to Hex String
    @staticmethod
    def int_list_to_hex_string(int_list: List[int], join: bool = True) -> str:
        """Convert a list of integers to a hex string.
        Example:
            Input: [72, 101, 108, 108, 111]
            Output: '48656c6c6f'
        """
        hex_list = ['{:02x}'.format(number) for number in int_list]
        return ''.join(hex_list) if join else hex_list
    
    # Hex string to Hex String Format (e.g., '48656c6c6f' -> '\\x48\\x65\\x6c\\x6c\\x6f')
    @staticmethod
    def hex_string_to_hex_string_format(hex_string: str) -> str:
        """Convert a hex string to a formatted hex string with each byte represented as '\\xHH'.
        Example:
            Input: '48656c6c6f'
            Output: '\\x48\\x65\\x6c\\x6c\\x6f'
        """
        return ''.join(f'\\x{hex_string[i:i + 2]}' for i in range(0, len(hex_string), 2))

    # Hex String Format to Hex String (e.g., '\x48\x65\x6c\x6c\x6f' -> '48656c6c6f')
    @staticmethod
    def hex_string_format_to_hex_string(hex_string_format: str) -> str:
        """Convert a formatted hex string (e.g., '\\xHH\\xHH') back to a hex string.
        Example:
            Input: '\\x48\\x65\\x6c\\x6c\\x6f'
            Output: '48656c6c6f'
        """
        return ''.join(hex_string_format[i + 2:i + 4] for i in range(0, len(hex_string_format), 4))


    # Bytes to Integer List
    @staticmethod
    def bytes_to_int_list(b: bytes) -> List[int]:
        """Convert a byte object to a list of integers.
        Example:
            Input: b'Hello'
            Output: [72, 101, 108, 108, 111]
        """
        return list(b)

    # Integer List to Bytes
    @staticmethod
    def int_list_to_bytes(int_list: List[int]) -> bytes:
        """Convert a list of integers to a byte object.
        Example:
            Input: [72, 101, 108, 108, 111]
            Output: b'Hello'
        """
        return bytes(int_list)

    # Float to Bytes
    @staticmethod
    def float_to_bytes(value: float) -> bytes:
        """Convert a float to a 4-byte representation.
        Example:
            Input: 12.34
            Output: b'\x41\x45\x70\xa4' (binary representation may vary)
        """
        return struct.pack('f', value)

    # Bytes to Float
    @staticmethod
    def bytes_to_float(b: bytes) -> float:
        """Convert a 4-byte representation to a float.
        Example:
            Input: b'\x41\x45\x70\xa4'
            Output: 12.34
        """
        return struct.unpack('f', b)[0]
    
    # Bytes to Hex String Format (single backslash)
    @staticmethod
    def bytes_to_hex_string_format(b: bytes) -> str:
        """Convert a byte object to a formatted hex string with each byte represented as '\\xHH'.
        Example:
            Input: b'Hello'
            Output: '\\x48\\x65\\x6c\\x6c\\x6f'
        """
        return ''.join(f'\\x{byte:02x}' for byte in b)

    # Hex String Format to Bytes
    @staticmethod
    def hex_string_format_to_bytes(hex_string_format: str) -> bytes:
        """Convert a formatted hex string (e.g., '\\xHH\\xHH') to a byte object.
        Example:
            Input: '\\x48\\x65\\x6c\\x6c\\x6f'
            Output: b'Hello'
        """
        return bytes(int(hex_string_format[i + 2:i + 4], 16) for i in range(0, len(hex_string_format), 4))

        
    # Integer to Integer List
    @staticmethod
    def int_to_int_list(n: int, specified_length: int = None, order: Literal["msb", "lsb"] = "msb") -> List[int]:
        """Convert an integer to a list of bytes, with optional byte order and length.
        Example:
            Input: 123456, specified_length=4, order='msb'
            Output: [0, 1, 226, 64]
        """
        byte_list = []
        while n:
            byte_list.append(n & 0xFF)
            n >>= 8
        if order == 'msb':
            byte_list.reverse()
        if specified_length is not None:
            additional_length = specified_length - len(byte_list)
            if additional_length < 0:
                raise ValueError("Specified length is less than the generated list length.")
            byte_list = ([0] * additional_length + byte_list) if order == 'msb' else (
                        byte_list + [0] * additional_length)
        return byte_list

    # Integer List to Integer
    @staticmethod
    def int_list_to_int(byte_list: List[int], order: Literal["msb", "lsb"] = "msb") -> int:
        """Convert a list of bytes to an integer, with optional byte order.
        Example:
            Input: [0, 1, 226, 64], order='msb'
            Output: 123456
        """
        if order == 'lsb':
            byte_list = byte_list[::-1]
        result = 0
        for byte in byte_list:
            result = (result << 8) | byte
        return result

    # Binary String to Integer List
    @staticmethod
    def bin_string_to_int_list(bin_string: str) -> List[int]:
        """Convert a binary string to a list of integers (8 bits per integer).
        Example:
            Input: '0100100001100101011011000110110001101111'
            Output: [72, 101, 108, 108, 111]
        """
        return [int(bin_string[i:i+8], 2) for i in range(0, len(bin_string), 8)]

    # Integer List to Binary String
    @staticmethod
    def int_list_to_bin_string(int_list: List[int]) -> str:
        """Convert a list of integers to a binary string.
        Example:
            Input: [72, 101, 108, 108, 111]
            Output: '0100100001100101011011000110110001101111'
        """
        return ''.join(f"{num:08b}" for num in int_list)

if __name__ == "__main__":
    tools = TypeEncodeDecodeTools()

    print("--- Testing int_list_to_str and str_to_int_list ---")
    int_list = [72, 101, 108, 108, 111]
    string = tools.int_list_to_str(int_list)
    print(f"int_list_to_str({int_list}): {string}")
    print(f"str_to_int_list('{string}'): {tools.str_to_int_list(string)}")

    print("\n--- Testing int_list_to_tuple and tuple_to_int_list ---")
    int_tuple = tools.int_list_to_tuple(int_list)
    print(f"int_list_to_tuple({int_list}): {int_tuple}")
    print(f"tuple_to_int_list({int_tuple}): {tools.tuple_to_int_list(int_tuple)}")

    print("\n--- Testing char_list_to_int_list and int_list_to_char_list ---")
    char_list = ['H', 'e', 'l', 'l', 'o']
    print(f"char_list_to_int_list({char_list}): {tools.char_list_to_int_list(char_list)}")
    print(f"int_list_to_char_list({int_list}): {tools.int_list_to_char_list(int_list)}")

    print("\n--- Testing char_list_to_str and str_to_char_list ---")
    print(f"char_list_to_str({char_list}): {tools.char_list_to_str(char_list)}")
    print(f"str_to_char_list('{string}'): {tools.str_to_char_list(string)}")

    print("\n--- Testing hex_string_to_int_list and int_list_to_hex_string ---")
    hex_string = "48656c6c6f"
    print(f"hex_string_to_int_list('{hex_string}'): {tools.hex_string_to_int_list(hex_string)}")
    print(f"int_list_to_hex_string({int_list}): {tools.int_list_to_hex_string(int_list)}")

    print("\n--- Testing bytes_to_int_list and int_list_to_bytes ---")
    byte_data = b"Hello"
    print(f"bytes_to_int_list({byte_data}): {tools.bytes_to_int_list(byte_data)}")
    print(f"int_list_to_bytes({int_list}): {tools.int_list_to_bytes(int_list)}")

    print("\n--- Testing float_to_bytes and bytes_to_float ---")
    float_value = 12.34
    float_bytes = tools.float_to_bytes(float_value)
    print(f"float_to_bytes({float_value}): {float_bytes}")
    print(f"bytes_to_float({float_bytes}): {tools.bytes_to_float(float_bytes)}")

    print("\n--- Testing bytes_to_hex_string_format and hex_string_format_to_bytes ---")
    formatted_hex = tools.bytes_to_hex_string_format(byte_data)
    print(f"bytes_to_hex_string_format({byte_data}): {formatted_hex}")
    print(f"hex_string_format_to_bytes('{formatted_hex}'): {tools.hex_string_format_to_bytes(formatted_hex)}")

    print("\n--- Testing int_to_int_list and int_list_to_int ---")
    integer_value = 123456
    int_list_from_int = tools.int_to_int_list(integer_value, specified_length=4, order="msb")
    print(f"int_to_int_list({integer_value}, 4, 'msb'): {int_list_from_int}")
    print(f"int_list_to_int({int_list_from_int}, 'msb'): {tools.int_list_to_int(int_list_from_int, 'msb')}")

    print("\n--- Testing bin_string_to_int_list and int_list_to_bin_string ---")
    binary_string = "0100100001100101011011000110110001101111"
    print(f"bin_string_to_int_list('{binary_string}'): {tools.bin_string_to_int_list(binary_string)}")
    print(f"int_list_to_bin_string({int_list}): {tools.int_list_to_bin_string(int_list)}")


    
