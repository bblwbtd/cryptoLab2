from scapy.all import sniff

# Capture only the ICMP package
# pkt = sniff(filter='icmp', prn=lambda p: p.show())

# Capture from a particular IP and port
# pkt = sniff(filter='src net 10.0.0.62 and dst port 23', prn=lambda p: p.show())

# Capture from a subnet
pkt = sniff(filter='src net 8.8.8.0/24', prn=lambda p: p.show()) 