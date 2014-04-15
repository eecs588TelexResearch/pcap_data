import dpkt
import socket
import sys
import pprint

#prints dest and src ips, along with packet counts for each file
#run from data_collection
def main():
    if len(sys.argv) < 3:
        print("Prints dest and src ips, along with packet counts for each file")
        print("Usage: pcap_ips.py <stream_dir> <number of files> <sorted(optional)>")
    directory_name = sys.argv[1]
    max_file = int(sys.argv[2])
    last_time = 0
    for i in range(0, max_file):
        ip_dict = {}
        packet_count = 0
        for ts, pkt in dpkt.pcap.Reader(open(directory_name + "/stream-" + str(i) + ".pcap", 'r')):
            packet_count += 1
            #counter += 1
            eth = dpkt.ethernet.Ethernet(pkt)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                    continue
            ip = eth.data
            #ipcounter += 1
            dst_ip_addr_str = socket.inet_ntoa(ip.dst)
            if dst_ip_addr_str in ip_dict:
                    ip_dict[dst_ip_addr_str] += 1
            else :
                    ip_dict[dst_ip_addr_str] = 1
        print("stream-" + str(i) + ".pcap: " + str(packet_count) + " packets")
        pprint.pprint(ip_dict)

if __name__ == "__main__":
    main()