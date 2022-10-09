from scapy.all import sr1
from scapy.layers.inet import IP, ICMP

def ping(dst: str, ttl=255):
    a = IP(dst=dst, src='10.0.0.62', ttl=ttl)
    b = ICMP()
    p = a/b/b' '
    return sr1(p, timeout=10)


if __name__ == '__main__':
    ping('8.8.8.8', ttl=20)
