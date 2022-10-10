#include <stdio.h>
#include <pcap.h>

void main()
{

    int sd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
    if (sd < 0)
    {
        perror("socket error");
        return;
    }

    struct sockaddr_in sin;
    sin.sin_family = AF_INET;

    char buffer[29] ="\x45\x00\x00\x1d\x00\x01\x00\x00\x14\x01\x54\xf7\x0a\xd3\x37\x06\x08\x08\x08\x08\x08\x00\xd7\xff\x00\x00\x00\x00\x20";

    int err = sendto(sd, buffer, 29, 0, (struct sockaddr *)&sin, sizeof(sin));
    if (err < 0)
    {
        perror("send error");
        return;
    }

    printf("sent package\n");
    return;
}
