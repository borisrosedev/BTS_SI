import sys 
import math

def get_cird(star_add:str, end_add:str):
    end_add_bits_groups = end_add.split(".")
    start_add_bits_groups = star_add.split(".")

    IPV4_ADDRESS_TOTAL_BITS = 32

    if not (len(end_add_bits_groups) == 4 and len(start_add_bits_groups) == 4):
        raise ValueError("IP Addresses must be composed of 32 bits")
    else:
        total_addresses_count = int(end_add_bits_groups[3]) - int(start_add_bits_groups[3]) + 1
        print("--------------------------------------------------------------")
        print("The total addresses count is {}".format(total_addresses_count))
        print("--------------------------------------------------------------")
        power = 0
        while total_addresses_count > math.pow(2, power):
            power = power + 1
        print("{0} bits are required to represent {1} addresses".format(power, total_addresses_count))
        print("--------------------------------------------------------------")
        print("The network corresponding to this range is 192.168.1.0/{}".format(IPV4_ADDRESS_TOTAL_BITS - power))
        print("--------------------------------------------------------------")
get_cird(star_add=sys.argv[1], end_add=sys.argv[2])