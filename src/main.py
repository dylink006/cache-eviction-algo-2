from fifo import FIFO
from lru import LRU
from optff import OPTFF
import sys

def main(filepath):
    try:
        with open(filepath, 'r') as f:
            line1 = f.readline().split()
            line2 = f.readline().split()
            max_size = int(line1[0])
            
            requests = []
            for n in line2:
                requests.append(int(n))
            
            fifo = FIFO(max_size)
            lru = LRU(max_size)
            optff = OPTFF(max_size, requests)

            for r in requests:
                fifo.take_request(r)
                lru.take_request(r)
            optff.take_requests()

            print(f"FIFO  : {fifo.misses}")
            print(f"LRU   : {lru.misses}")
            print(f"OPTFF : {optff.misses}")
    except FileNotFoundError:
        print("Bad file path, file does not exist.")

        


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            main(arg)
    else:
        print("No filepath given. Usage: python3 main.py <filename1> <optional filenames...>")