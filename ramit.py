import sys
import time
from memory_profiler import profile
import shutil

chunks=100
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


heading1 = "RAMIT"
heading2 = "================================================================================================="
heading3 = "This console application will allow you to consume a given amount of RAM for a given time"
print()
print_centre(heading1)
print_centre(heading2)
print_centre(heading3)
print_centre(heading2)
print()
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

