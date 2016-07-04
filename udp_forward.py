"""
Usage:
    udp_forward.py <fport> <thost> <tport> [--debug]

Example:
    dod -p 8125:8125/udp -v $(pwd):/code tangyouze/qbbase:0.0.5 python /code/udp_forward.py 8125 ntu.prod.telegraf.weave.local 8125 --debug
"""
from docopt import docopt as __docopt
import socket

docopt = __docopt(__doc__)
docopt['<fport>'] = int(docopt['<fport>'])
docopt['<tport>'] = int(docopt['<tport>'])
print(docopt)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", docopt['<fport>']))
print("waiting on port:", docopt['<fport>'])
while 1:
    data, addr = s.recvfrom(1024)
    s.sendto(data, (docopt['<thost>'], docopt['<tport>']))
    if docopt['--debug']:
        print(data)

# import socket  # for sockets
# import sys  # for exit

# create dgram udp socket
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# except socket.error:
#     print
#     'Failed to create socket'
#     sys.exit()
#
# host = 'localhost';
# port = 8888;
#
# while (1):
#     msg = raw_input('Enter message to send : ')
#
#     try:
#         # Set the whole string
#
#         # receive data from client (data, addr)
#         d = s.recvfrom(1024)
#         reply = d[0]
#         addr = d[1]
