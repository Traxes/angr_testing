# angr_testing

output of angr:

```
0xffffffff
Value Should be 0x41414141 to really bypass this fucker
0x41414141
DEBUG   | 2017-02-18 21:11:22,702 | angr.path_group | Round 0: stepping <PathGroup with 2 active>
DEBUG   | 2017-02-18 21:11:22,716 | angr.path_group | Round 1: stepping <PathGroup with 2 active>
DEBUG   | 2017-02-18 21:11:22,729 | angr.path_group | Round 2: stepping <PathGroup with 2 active>
DEBUG   | 2017-02-18 20:45:28,480 | angr.path_group | Round 19: stepping <PathGroup with 1 deadended, 32 active>
DEBUG   | 2017-02-18 20:45:30,600 | angr.path_group | Round 20: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 20:45:31,925 | angr.path_group | Round 21: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 20:45:33,136 | angr.path_group | Round 22: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 20:45:37,219 | angr.path_group | Round 23: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 20:45:40,506 | angr.path_group | Round 24: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 20:45:42,063 | angr.path_group | Round 25: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 20:45:50,859 | angr.path_group | Round 26: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 20:45:57,311 | angr.path_group | Round 27: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 20:46:01,907 | angr.path_group | Round 28: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 20:46:17,827 | angr.path_group | Round 29: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 20:46:33,743 | angr.path_group | Round 30: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 20:46:40,124 | angr.path_group | Round 31: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 20:47:16,234 | angr.path_group | Round 32: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 20:47:42,225 | angr.path_group | Round 33: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 20:48:01,483 | angr.path_group | Round 34: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 20:49:13,648 | angr.path_group | Round 35: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 21:11:23,351 | angr.path_group | Round 10: stepping <PathGroup with 1 deadended, 4 active>
DEBUG   | 2017-02-18 20:50:07,162 | angr.path_group | Round 36: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 20:50:32,659 | angr.path_group | Round 37: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 20:52:59,278 | angr.path_group | Round 38: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 20:55:01,002 | angr.path_group | Round 39: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 20:55:52,147 | angr.path_group | Round 40: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 21:00:37,536 | angr.path_group | Round 41: stepping <PathGroup with 1 deadended, 8192 active>
DEBUG   | 2017-02-18 21:04:06,893 | angr.path_group | Round 42: stepping <PathGroup with 1 deadended, 8192 active>
^CStopping Execution for Debug. If you want to kill the programm issue: killmyself()
Python 2.7.10 (default, Oct 14 2015, 16:09:02)
Type "copyright", "credits" or "license" for more information.

IPython 5.2.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
DEBUG   | 2017-02-18 21:11:23,594 | angr.path_group | Round 11: stepping <PathGroup with 1 deadended, 8 active>
DEBUG   | 2017-02-18 21:11:23,764 | angr.path_group | Round 12: stepping <PathGroup with 1 deadended, 8 active>
DEBUG   | 2017-02-18 21:11:23,864 | angr.path_group | Round 13: stepping <PathGroup with 1 deadended, 8 active>
DEBUG   | 2017-02-18 21:11:24,507 | angr.path_group | Round 14: stepping <PathGroup with 1 deadended, 16 active>
DEBUG   | 2017-02-18 21:11:24,844 | angr.path_group | Round 15: stepping <PathGroup with 1 deadended, 16 active>
DEBUG   | 2017-02-18 21:11:25,041 | angr.path_group | Round 16: stepping <PathGroup with 1 deadended, 16 active>
DEBUG   | 2017-02-18 21:11:26,180 | angr.path_group | Round 17: stepping <PathGroup with 1 deadended, 32 active>
DEBUG   | 2017-02-18 21:11:27,120 | angr.path_group | Round 18: stepping <PathGroup with 1 deadended, 32 active>
DEBUG   | 2017-02-18 21:11:27,518 | angr.path_group | Round 19: stepping <PathGroup with 1 deadended, 32 active>
DEBUG   | 2017-02-18 21:11:29,670 | angr.path_group | Round 20: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 21:11:31,016 | angr.path_group | Round 21: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 21:11:32,240 | angr.path_group | Round 22: stepping <PathGroup with 1 deadended, 64 active>
DEBUG   | 2017-02-18 21:11:36,386 | angr.path_group | Round 23: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 21:11:39,729 | angr.path_group | Round 24: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 21:11:41,328 | angr.path_group | Round 25: stepping <PathGroup with 1 deadended, 128 active>
DEBUG   | 2017-02-18 21:11:50,272 | angr.path_group | Round 26: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 21:11:56,830 | angr.path_group | Round 27: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 21:12:01,492 | angr.path_group | Round 28: stepping <PathGroup with 1 deadended, 256 active>
DEBUG   | 2017-02-18 21:12:17,617 | angr.path_group | Round 29: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 21:12:32,758 | angr.path_group | Round 30: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 21:12:39,184 | angr.path_group | Round 31: stepping <PathGroup with 1 deadended, 512 active>
DEBUG   | 2017-02-18 21:13:15,342 | angr.path_group | Round 32: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 21:13:41,611 | angr.path_group | Round 33: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 21:14:00,018 | angr.path_group | Round 34: stepping <PathGroup with 1 deadended, 1024 active>
DEBUG   | 2017-02-18 21:15:11,763 | angr.path_group | Round 35: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 21:16:06,014 | angr.path_group | Round 36: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 21:16:32,060 | angr.path_group | Round 37: stepping <PathGroup with 1 deadended, 2048 active>
DEBUG   | 2017-02-18 21:18:53,259 | angr.path_group | Round 38: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 21:20:57,720 | angr.path_group | Round 39: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 21:21:49,520 | angr.path_group | Round 40: stepping <PathGroup with 1 deadended, 4096 active>
DEBUG   | 2017-02-18 21:26:33,600 | angr.path_group | Round 41: stepping <PathGroup with 1 deadended, 8192 active>
DEBUG   | 2017-02-18 21:30:03,895 | angr.path_group | Round 42: stepping <PathGroup with 1 deadended, 8192 active>
DEBUG   | 2017-02-18 21:32:37,865 | angr.path_group | Round 43: stepping <PathGroup with 1 deadended, 8192 active>
DEBUG   | 2017-02-18 21:42:23,032 | angr.path_group | Round 44: stepping <PathGroup with 1 deadended, 16384 active>
DEBUG   | 2017-02-18 21:49:35,983 | angr.path_group | Round 45: stepping <PathGroup with 1 deadended, 16384 active>
DEBUG   | 2017-02-18 21:54:59,579 | angr.path_group | Round 46: stepping <PathGroup with 1 deadended, 16384 active>
DEBUG   | 2017-02-19 02:52:52,217 | angr.path_group | Round 47: stepping <PathGroup with 1 deadended, 32768 active>
```

killed it here after 12 Hours of execution and 64 Gig of mem allocated
