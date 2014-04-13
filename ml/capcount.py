# datagen.py
# generates CSV .data file for input to svmachine.py
# Requires DPKT by Dug Song & Jon Oberheide, available here: code.google.com/p/dpkt/downloads/list

# run like:
# python datagen.py > filename.data

from __future__ import print_function
import dpkt
import socket
import sys
import pprint
import operator


def main():
    max_file = int(sys.argv[1])
    last_time = 0
    flows = {}
    for i in range(0, max_file):
        packet_count = 0
        for ts, pkt in dpkt.pcap.Reader(open("streams/stream-" + str(i) + ".pcap", 'r')):
            packet_count += 1
        flows[i] = packet_count

    #pprint.pprint(flows)
    # sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
    sorted_flows = sorted(flows.values())
    for key in sorted_flows:
        print(key)


if __name__ == "__main__":
    main()


