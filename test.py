from os import system, popen
import ctypes


__NR_mysyscall__ = 333

# Clear dmesg
_ = popen('dmesg -c').read()

# Make a system call
libc = ctypes.CDLL(None)
syscall = libc.syscall
syscall(__NR_mysyscall__)

# Get the contents from kernel print
raw = popen('dmesg').readlines()[1:-1]
content = [line[:-1].split('\t') for line in raw]
print('Total page faults:', content[0][1])
print('Page fault for current process:', content[0][0].strip())
print('Dirty page count for all processes:')
for c in content[1:]:
    print('Process %s: %s, dirty page: %s' % (c[0][c[0].find(']')+2:], c[1], c[2]))
