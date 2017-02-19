import angr
import simuvex
import IPython
import signal
import os
import claripy



##Debug Help##

def killmyself():
    os.system('kill %d' % os.getpid())

def sigint_handler(signum, frame):
    print 'Stopping Execution for Debug. If you want to kill the programm issue: killmyself()'
    IPython.embed()

signal.signal(signal.SIGINT, sigint_handler)



#Input 38 Chars long
#input_size = 0x26
input_size = 38

# Function for compare keys
avoid_addr = 0x400c06

find_addr = 0x400cae

b = angr.Project("./antidebug")

# Hooking nonsense antidebug
b.hook(0x4008cd, angr.Hook(simuvex.SimProcedures['stubs']['ReturnUnconstrained']), kwargs={'resolves': 'nothing'})
b.hook(0x4006c0, angr.Hook(simuvex.SimProcedures['stubs']['ReturnUnconstrained']), kwargs={'resolves': 'nothing'})

argv1 = angr.claripy.BVS("argv1", input_size * 8)

initial_state = b.factory.entry_state(args=["./antidebug", argv1], add_options={"BYPASS_UNSUPPORTED_SYSCALL"})


# Limit input on only printable chars
for byte in argv1.chop(8):
    initial_state.add_constraints(byte != '\x00') # null
    initial_state.add_constraints(byte >= ' ') # '\x20'
    initial_state.add_constraints(byte <= '~') # '\x7e'



# Patch Sigint loop
ignore = claripy.BVV(0x41414141, 32)
print hex(initial_state.se.any_int(initial_state.memory.load(0x6021d8, 4, endness='Iend_LE')))
initial_state.memory.store(0x6021d8, ignore)
print "Value Should be 0x41414141 to really bypass this fucker"
print hex(initial_state.se.any_int(initial_state.memory.load(0x6021d8, 4, endness='Iend_LE')))


# Init Path Group
initial_path = b.factory.path(initial_state)
pg = b.factory.path_group(initial_state)


# Step until first branch (Should initialize the checksum correctly)
pg.step(until=lambda lpg: len(lpg.active) > 1)

# Debug for more information
angr.path_group.l.setLevel("DEBUG")

# Drop avoid paths instantly (Better for memory)
pg.explore(find=find_addr, avoid=avoid_addr, step_func=lambda lpg: lpg.drop(stash='avoid'))

#print("Flag?")
#print(pg.found[0].state.se.any_str(argv1))

IPython.embed()