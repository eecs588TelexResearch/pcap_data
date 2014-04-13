import dpkt
import socket
import sys
import pprint

def main():
	ip_dict = {}
	filename = sys.argv[1]
	last_time = 0
	for ts, pkt in dpkt.pcap.Reader(open(filename, 'r')):
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

	pprint.pprint(ip_dict)

if __name__ == "__main__":
    main()
