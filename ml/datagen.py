# datagen.py
# generates CSV .data file for input to svmachine.py
# Requires DPKT by Dug Song & Jon Oberheide, available here: code.google.com/p/dpkt/downloads/list

# run like:
# python datagen.py > filename.data

from __future__ import print_function
import dpkt
import socket

def dnsLookup(dst_ip):
	try:
		tuple = socket.gethostbyaddr(dst_ip)
		return tuple[0]
	except socket.herror:
		return "ERROR"

def isBlocked(dst_ip):
	name = dnsLookup(dst_ip)
	#print(name)
	#return False
	return name == 'ord08s08-in-f16.1e100.net'
   

 #return dst_ip == '141.212.109.161'

filename   =  'google_pageload_std_v2 copy.pcapng'
filename1  =  'google_interaction.s0i0.pcap'
filename2  =  'google_pageload_std_v2 copy.s0i0'
filename3  =  'google_pageload_std_v2 copy.s0i0.pcap'

#counter = 0
#ipcounter = 0
#tcpcounter = 0
#udpcounter = 0

last_time = 0

for ts, pkt in dpkt.pcap.Reader(open(filename1, 'r')):
	#counter += 1
	eth = dpkt.ethernet.Ethernet(pkt)
	if eth.type != dpkt.ethernet.ETH_TYPE_IP:
		continue
	ip = eth.data
    #ipcounter += 1
	dst_ip_addr_str = socket.inet_ntoa(ip.dst)
	if last_time == 0:
		delta = 0
	else:
		delta = ts - last_time

	last_time = ts

	# size, time delta, is dest IP blocked
	print( len(pkt),",",delta,",",isBlocked(dst_ip_addr_str), sep='')

#if ip.p == dpkt.ip.IP_PROTO_TCP:
#		tcpcounter += 1
#	elif ip.p == dpkt.ip.IP_PROTO_UDP:
#		udpcounter += 1

#print "Total number of packets in the pcap file: ", counter
#print "Total number of ip packets: ", ipcounter
#print "Total number of tcp packets: ", tcpcounter
#print "Total number of udp packets: ", udpcounter

