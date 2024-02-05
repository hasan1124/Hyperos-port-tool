#!/usr/bin/env python
import sys
if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(f"Usage: python ./{sys.argv[0]} <vbmeta-image>")

    FILE = sys.argv[1]
    with open(FILE, 'rb+') as vbmeta:
        if vbmeta.read(4) != b"AVB0":
            sys.exit("Error: The provided image is not a valid vbmeta image.\nFile not modified. Exiting...")
        vbmeta.seek(123, 0)
        vbmeta.write(b'\x03')
        print("Patch Done!")
