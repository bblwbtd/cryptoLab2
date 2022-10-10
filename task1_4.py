
from scapy.all import sniff, Packet, send
from scapy.layers.inet import ICMP, IP

def make_ping_response(dst: str, src: str, icmp_request: ICMP):
    ip = IP(dst=dst, src=src)
    icmp = icmp_request.copy()
    icmp.type = 0
    icmp.chksum = None
    response = ip/icmp
    return response


def handle_package(p: Packet): 
    ip = p.getlayer(IP)
    response = make_ping_response(ip.src, ip.dst, p.getlayer(ICMP))
    send(response)
    

sniff(filter='icmp', prn=handle_package)
