import sys
import time
from memory_profiler import profile

chunks=100
endMemory = int(input("Enter RAM (in MB) you want to allocate : "))
print()
t = int(input("For how long you want to keep? (in sec) : "))
print()

@profile
def run():
	x = bytearray()
	mem = 0
	while sys.getsizeof(x)<=(endMemory*(10**6)):
		mem = mem+chunks
		x = bytearray(1024*1024*mem)
	print("==================================")
	print()
	print("Memory allocated")
	print()
	print("==================================")
	time.sleep(t)
	del x

	print()
	print("Memory deallocated")
	print()
	print("==================================")
	
run()

input("Press any key to exit.....")

