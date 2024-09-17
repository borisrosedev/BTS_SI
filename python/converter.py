from typing import List
from abc import ABC, abstractmethod
import math

class ConvertingStrategy(ABC):
    @abstractmethod
    def convert(self): 
        pass


class IPAddressConvertingStrategy(ConvertingStrategy):
    def __init__(self, val: str) -> None:
        self.val = val;
    def convert_8_bits_group(self, bits_group: str):
        bits = []
        while True:
            if math.floor(float(bits_group) / 2) == 0:
                left = str(float(bits_group) % 2)
                bits.append(left.split(".")[0]) 
                break;
            else:
                left = str(float(bits_group) % 2)
                bits.append(left.split(".")[0]) 
                bits_group = str(float(bits_group) / 2)
        if len(bits) < 8:
            while len(bits) < 8:
                bits.append("0") 
        bits.reverse()
        return "".join(bits)
        
    def convert(self):
        if not isinstance(self.val, str) :
            raise TypeError("IP Address must be a string")
        else:
            bits_groups: List[str] = self.val.split(".")
            if not len(bits_groups) == 4:
                raise ValueError("IP Address must have 32 bits")
            else:
                formatted_groups = [];
                for bits_group in bits_groups:
                    if len(bits_group) < 3 :
                        while not len(bits_group) == 3:
                            bits_group = "0" + bits_group
                    elif len(bits_group) > 3:
                        raise ValueError("ID Address must be made of 4 decimals of 8 bits")
                    else:
                        pass
                    formatted_groups.append(bits_group)
                #['192', '168', '001', '010']
                binary_bits_groups = []
                for bits_group in formatted_groups:
                    binary_bits_groups.append(self.convert_8_bits_group(bits_group=bits_group))
                print(".".join(binary_bits_groups))

class BinaryToDecimalConvertingStrategy(ConvertingStrategy):
    def __init__(self, val: str) -> None:
        self.val = val;

    def convert(self):
        power = 7
        result = 0;
        for string_number in self.val:
            if int(string_number) == 1:
                 result += (1 * 2**power)
            else:
                result += (0 * 2**power) 
            power = power - 1
            if power == -1:
                break;
        print(result)
            
class BinaryToHexadecimalConvertingStrategy(ConvertingStrategy):
    def __init__(self, val: str) -> None:
        self.val = val 
    
    def convert(self):
        if len(self.val) % 4 != 0:
            self.val = "0" + self.val
            self.convert()
        else:
            count = 0
            bit_groups = []
            bit_group = ""
            for index, number in enumerate(self.val):
                if count < 4:
                    bit_group += number
                    count += 1
                    if len(self.val) - 1 == index:
                        bit_groups.append(bit_group)
                else :
                    count = 0 
                    bit_groups.append(bit_group)
                    bit_group = ""
                    bit_group += number
                    count += 1        
            if len(bit_groups) > 0:
                decimal_groups = []
                for group in bit_groups:
                    power = 3
                    result = 0
                    for number in group:
                        if int(number) == 1:
                            result += (1 * 2**power) 
                        else:
                            result += (0 * 2**power)
                        power -= 1
                    decimal_groups.append(str(result))
                if len(decimal_groups):
                    hexadecimal = "";
                    for decimal_group in decimal_groups:
                        if int(decimal_group) in range(0,10):
                            hexadecimal += decimal_group
                        elif int(decimal_group) in [10,11,12,13,14,15]:
                            chars = ["A", "B", "C", "D", "E", "F"]
                            if int(decimal_group) == 10: 
                                hexadecimal += chars[0]
                            if int(decimal_group) == 11: 
                                hexadecimal += chars[1]
                            if int(decimal_group) == 12: 
                                hexadecimal += chars[2]
                            if int(decimal_group) == 13: 
                                hexadecimal += chars[3]
                            if int(decimal_group) == 14: 
                                hexadecimal += chars[4]
                            if int(decimal_group) == 15: 
                                hexadecimal += chars[5]
                    print(hexadecimal)

class Converter: 
    def __init__(self, strategy: ConvertingStrategy) -> None: 
        self.strategy = strategy
    
    def convert(self):
        self.strategy.convert()
        


#converter = Converter(BinaryToDecimalConvertingStrategy("11001101"))
# 10110110 doit donner 182
# 11001101 doit donner 205

converter = Converter(IPAddressConvertingStrategy("192.168.1.10"))

converter.convert()


        

    

        