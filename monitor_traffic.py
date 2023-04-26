# sudo stdbuf --output=0 tcpdump -i any -nnnv "tcp[tcpflags]=(tcp-syn)" | python3 monitor_traffic.py


# Python imports
import sys
import os


    

def main():

    print ("Monitor ready")

    #service_list = []

    while True:
        line = sys.stdin.readline()
        line = line.strip()
        traffic = line.split(':')

        if ">" in traffic[0]:
            print ("OUT: ", traffic[0])
            target_port = traffic[0].split('.')
            target_port = target_port[8]
            print("PORT:", target_port)

            #if target_port not in service_list:
            #    service_list.append(target_port)
            nc_listener = "screen -d -m nc -lnvp " + target_port 
            os.system(nc_listener)

if __name__ == '__main__':
    sys.exit(main())
