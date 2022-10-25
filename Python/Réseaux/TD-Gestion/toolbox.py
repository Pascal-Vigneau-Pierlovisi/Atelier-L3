from datetime import datetime
from struct import *
import time


def encode_message(mess: str) -> bytes:
    compact = pack('>f', time.time()) + mess.encode()
    size = len(compact)
    mess_encoded = pack(">I", size) + compact
    return mess_encoded


def decode_message(b: bytes) -> str:
    time = b[0:4]
    time = unpack('>f', time)
    mess = b[4:].decode()
    date = datetime.fromtimestamp(time[0])
    res = str(date) + " " + str(mess)
    return res


if __name__ == '__main__':
    mess = "Hello world"
    print(encode_message(mess))
    compact = pack('>f', time.time()) + mess.encode()
    print(decode_message(compact))
