#!/bin/sh

for stream in `tshark -r $1 -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r $1 -F pcap -w streams/stream-$stream.pcap -Y "tcp.stream==$stream"
done
