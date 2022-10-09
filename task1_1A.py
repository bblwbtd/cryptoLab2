from scapy.all import sniff


pkt = sniff(filter='icmp', prn=lambda p: p.show())
