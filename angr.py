import angr
import simuvex
import IPython
import signal
import os
import claripy
from simuvex import SimProcedure


def killmyself():
    os.system('kill %d' % os.getpid())

def sigint_handler(signum, frame):
    print 'Stopping Execution for Debug. If you want to kill the programm issue: killmyself()'
    IPython.embed()

signal.signal(signal.SIGINT, sigint_handler)

fixpideax = claripy.BVV(0x00000030, 32)
class fixpid(SimProcedure):
    def run(self):
            print("Jumped into Hook :)")
            return 0x30
       


#Input 38 Chars long
#input_size = 0x26
input_size = 38



find_addr = 0x400cae

b = angr.Project("./antidebug")


b.hook(0x4008cd, fixpid, length=5)
b.hook(0x4006c0, angr.Hook(simuvex.SimProcedures['stubs']['ReturnUnconstrained']), kwargs={'resolves': 'nothing'})


argv1 = angr.claripy.BVS("argv1", input_size * 8)

#initial_state = b.factory.full_init_state(args=["./antidebug", argv1], add_options={"BYPASS_UNSUPPORTED_SYSCALL"}, add_options=simuvex.o.unicorn, remove_options={simuvex.o.LAZY_SOLVES})
initial_state = b.factory.entry_state(args=["./antidebug", argv1], add_options={"BYPASS_UNSUPPORTED_SYSCALL"})

for byte in argv1.chop(8):
    initial_state.add_constraints(byte != '\x00') # null
    initial_state.add_constraints(byte >= ' ') # '\x20'
    initial_state.add_constraints(byte <= '~') # '\x7e'

#initial_state.add_constraints(argv1.chop(8)[38] == '\x00')

# Patch Sigint loop
ignore = claripy.BVV(0x41414141, 32)
setback = claripy.BVV(0xFFFFFFFF,32)
print hex(initial_state.se.any_int(initial_state.memory.load(0x6021d8, 4, endness='Iend_LE')))
initial_state.memory.store(0x6021d8, ignore)

print "Value Should be 0x41414141 to really bypass this fucker"
print hex(initial_state.se.any_int(initial_state.memory.load(0x6021d8, 4, endness='Iend_LE')))



initial_path = b.factory.path(initial_state)
pg = b.factory.path_group(initial_state)


pg.step(until=lambda lpg: len(lpg.active) > 1)

for states in pg.active:
    if states.addr == 0x400ae2:
        s = states.state
        s.memory.store(0x6021d8, setback)
        print("Check the hook result: should be 0x30")
        print hex(s.se.any_int(s.memory.load(0x6021f2, 1, endness='Iend_LE')))
        print("Check if bypass int3 is again: 0xffffffff")
        print hex(s.se.any_int(s.memory.load(0x6021d8, 4, endness='Iend_LE')))
IPython.embed()


angr.path_group.l.setLevel("DEBUG")
avoid_addr = 0x400c06 # WrongKey
avoid_addr2 = 0x400bc7 # AntiDebug
avoid_addr3 = 0x400cba # BAD
avoid_addr4 = 0x400ad8 # BAD2
avoid_addr5 = 0x40089d # BAD3



pg.explore(find=find_addr, avoid=[avoid_addr, avoid_addr2, avoid_addr3, avoid_addr4, avoid_addr5], step_func=lambda lpg: lpg.drop(stash='avoid'))

IPython.embed()
