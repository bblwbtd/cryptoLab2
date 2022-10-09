from task1_2 import ping


def trace_route(dst: str):
    for i in range(1,255):
        print(f"Sending a packet. ttl={i}")
        rec = ping(dst, ttl=i)
        if rec is None:
            print(f"No Response for the packet")
        else:
            print(f"Got Response from packet, {rec.src}")
            if rec.src == dst:
                print(f"ttl is {i}")
                break


if __name__ == '__main__':
    trace_route('172.253.62.139')
