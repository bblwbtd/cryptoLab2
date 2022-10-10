# Reuse code from previous task
from task1_2 import ping

def trace_route(dst: str):
    # Try ttl from 1 to 255
    for i in range(1,255):
        print(f"Sending a packet. ttl={i}")
        # Use ping function from previous task.
        rec = ping(dst, ttl=i)
        if rec is None:
            print(f"No Response for the packet")
        else:
            print(f"Got Response from ip {rec.src}")
            if rec.src == dst:
                print(f"ttl is {i}")
                break

if __name__ == '__main__':
    trace_route('128.220.192.230')
