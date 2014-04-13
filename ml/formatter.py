

from __future__ import print_function
import dpkt
import socket
import sys
import pprint
import operator


def main():
    max_file = int(sys.argv[1])
    flows = {}

    print(max_file)

    for i in range(0, max_file):
        last_time = 0
        packet_count = 0
        list_of_packetLists = []
        for ts, pkt in dpkt.pcap.Reader(open("streams/stream-" + str(i) + ".pcap", 'r')):

            eth = dpkt.ethernet.Ethernet(pkt)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                print("DROP")
                continue
            ip = eth.data

            packet_count += 1

            dst_ip_addr_str = socket.inet_ntoa(ip.dst)
            if last_time == 0:
                delta = 0
            else:
                delta = ts - last_time

            last_time = ts

            packetList = [ ts, len(pkt), delta, dst_ip_addr_str ]
            list_of_packetLists.append(packetList)

        flows[i] = [packet_count, list_of_packetLists]
        if packet_count <= 50:
            print("Baidu")
        else:
            print("Google")
        print(packet_count)
        for pl in list_of_packetLists:
            classification = ""
            if pl[3].find("35.2") == 0 :
                classification = "recv"
            else :
                classification = "send"
            print(pl[1], pl[2], classification)



if __name__ == "__main__":
    main()
