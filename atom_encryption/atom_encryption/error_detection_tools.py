class ErrorDetectionTools:
    """
    A collection of error detection tools including BCC, CRC (12, 16, 32), parity check, and LRC.
    """

    @staticmethod
    # support algorithm print
    def supported_algorithms():
        """
        Print the supported error detection algorithms.
        """
        print("Supported Error Detection Algorithms:")
        print("1. BCC (Block Check Character)")
        print("2. CRC (Cyclic Redundancy Check)")
        print("3. Parity Check (Even and Odd Parity)")
        print("4. LRC (Longitudinal Redundancy Check)")


    class BCC:
        """
        BCC (Block Check Character) for simple XOR checksum.
        """
        @staticmethod
        def generate(data: bytes) -> int:
            """
            Generate BCC for the given data.
            Args:
                data (bytes): Input data as bytes.
            Returns:
                int: BCC checksum value.
            """
            bcc = 0
            for byte in data:
                bcc ^= byte
            return bcc

        @staticmethod
        def verify(data: bytes, checksum: int) -> bool:
            """
            Verify if the BCC checksum matches the data.
            Args:
                data (bytes): Input data as bytes.
                checksum (int): BCC checksum to verify against.
            Returns:
                bool: True if valid, False otherwise.
            """
            return ErrorDetectionTools.BCC.generate(data) == checksum

    class CRC:
        """
        CRC (Cyclic Redundancy Check) with support for CRC-12, CRC-16, and CRC-32.
        """
        @staticmethod
        def generate(data: bytes, polynomial: int, width: int, init_value: int = 0) -> int:
            """
            Generate CRC checksum for the given data.
            Args:
                data (bytes): Input data as bytes.
                polynomial (int): CRC polynomial.
                width (int): Width of the CRC (e.g., 12, 16, 32).
                init_value (int): Initial value for the CRC computation.
            Returns:
                int: CRC checksum value.
            """
            crc = init_value
            for byte in data:
                crc ^= byte << (width - 8)
                for _ in range(8):
                    if crc & (1 << (width - 1)):
                        crc = (crc << 1) ^ polynomial
                    else:
                        crc <<= 1
                    crc &= (1 << width) - 1  # Mask to width
            return crc

        @staticmethod
        def verify(data: bytes, checksum: int, polynomial: int, width: int, init_value: int = 0) -> bool:
            """
            Verify CRC checksum matches the data.
            Args:
                data (bytes): Input data as bytes.
                checksum (int): CRC checksum to verify against.
                polynomial (int): CRC polynomial.
                width (int): Width of the CRC (e.g., 12, 16, 32).
                init_value (int): Initial value for the CRC computation.
            Returns:
                bool: True if valid, False otherwise.
            """
            return ErrorDetectionTools.CRC.generate(data, polynomial, width, init_value) == checksum

    class Parity:
        """
        Parity check for even and odd parity.
        """
        @staticmethod
        def generate(data: bytes, even_parity: bool = True) -> int:
            """
            Generate parity bit for the given data.
            Args:
                data (bytes): Input data as bytes.
                even_parity (bool): Use even parity if True, odd parity otherwise.
            Returns:
                int: Parity bit (0 or 1).
            """
            bit_count = sum(bin(byte).count('1') for byte in data)
            parity_bit = 0 if (bit_count % 2 == 0) else 1
            return parity_bit if even_parity else 1 - parity_bit

        @staticmethod
        def verify(data: bytes, parity_bit: int, even_parity: bool = True) -> bool:
            """
            Verify the parity bit for the given data.
            Args:
                data (bytes): Input data as bytes.
                parity_bit (int): Parity bit to verify (0 or 1).
                even_parity (bool): Use even parity if True, odd parity otherwise.
            Returns:
                bool: True if valid, False otherwise.
            """
            return ErrorDetectionTools.Parity.generate(data, even_parity) == parity_bit

    class LRC:
        """
        LRC (Longitudinal Redundancy Check).
        """
        @staticmethod
        def generate(data: bytes) -> int:
            """
            Generate LRC for the given data.
            Args:
                data (bytes): Input data as bytes.
            Returns:
                int: LRC checksum value.
            """
            lrc = 0
            for byte in data:
                lrc = (lrc + byte) & 0xFF
            return (-lrc) & 0xFF

        @staticmethod
        def verify(data: bytes, checksum: int) -> bool:
            """
            Verify if the LRC checksum matches the data.
            Args:
                data (bytes): Input data as bytes.
                checksum (int): LRC checksum to verify against.
            Returns:
                bool: True if valid, False otherwise.
            """
            return ErrorDetectionTools.LRC.generate(data) == checksum

if __name__ == "__main__":
    # Example usage
    data = b"123456789"

    # BCC Example
    bcc = ErrorDetectionTools.BCC.generate(data)
    print(f"BCC: {bcc}, Verified: {ErrorDetectionTools.BCC.verify(data, bcc)}")

    # CRC Example (CRC-16-CCITT)
    crc16 = ErrorDetectionTools.CRC.generate(data, polynomial=0x1021, width=16, init_value=0xFFFF)
    print(f"CRC-16: {crc16}, Verified: {ErrorDetectionTools.CRC.verify(data, crc16, polynomial=0x1021, width=16, init_value=0xFFFF)}")

    # Parity Example
    parity = ErrorDetectionTools.Parity.generate(data, even_parity=True)
    print(f"Parity Bit: {parity}, Verified: {ErrorDetectionTools.Parity.verify(data, parity, even_parity=True)}")

    # LRC Example
    lrc = ErrorDetectionTools.LRC.generate(data)
    print(f"LRC: {lrc}, Verified: {ErrorDetectionTools.LRC.verify(data, lrc)}")
