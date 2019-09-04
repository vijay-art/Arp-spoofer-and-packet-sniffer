#!usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn= packet_sniffer)

def packet_sniffer(packet):
    
    if packet.haslayer(http.HTTPRequest):
       url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
       print(url)

       if packet.haslayer(scapy.Raw):
           print(packet[scapy.Raw].load)
 
interface = input("enter your interface > ")

sniffer(interface)
