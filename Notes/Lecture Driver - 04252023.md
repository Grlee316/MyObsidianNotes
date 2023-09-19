![[Pasted image 20230425174041.png]]
Green only appear at the user space
RTOS -> Real Time Operating Systems
you know when something will happen

![[Pasted image 20230425174358.png]]

Too much code there, you

![[Pasted image 20230425174546.png]]

path of the operating system
part of the kernel
only one process

you can load and unload this thing
there are two ways to load
automatically load
Inser this module by Hand

![[Pasted image 20230425174911.png]]

Very important line:


![[Pasted image 20230425175048.png]]
you can move sig pointer into the file
you don't want to read the full file from the memory


First example of the driver:
![[Pasted image 20230425175137.png]]

Printk -> instead of printf

it will be logged at the kernel log file
printk -> all the module that poped up
This is a simple example of using ioctl in a Linux device driver. If you want to send multiple arguments, put those variables into the structure, and pass the address of the structure.

In our next tutorial, we will see another userspace and kernel space communication method which is procfs.

Please find the other Linux device driver tutorials here.

You can also read the below tutorials.
define some parameters
how can i tell the header file is located

![[Pasted image 20230425175606.png]]
cann make file
this file name cannot be changed
(makefile)

you can specify different kind of files, when you copy thesecodes, you need to save it as Makefile and save it like that
if you don't see .ko inside, something is mesed up.

This process run on the super user
high pervillage mode:
![[Pasted image 20230425180151.png]]

sometimes it will not work
half of the class will not pay attention at the top part

![[Pasted image 20230425180241.png]]
subdirectories of the update that you did on your kernel
**you can only compile the module against source file that will use the compile the kernel itself (current kernel)**

uname -a

kernel will reject if the version is different
the system already update the file
but you havent do sudo apt update yet

Makefile


if you get 
## Tainted module
it means your module does not match

![[Pasted image 20230425180732.png]]

when you insert this module the function that get executed is the function that you assign in the module_init
![[Pasted image 20230425180944.png]]

When you remove the module, the exit function will get executed (assign the function ece_end) dmesg log screen will show the last one (ece_end)

-D standard defines in the C file
for this code to be compiled as a modules, this macros need to be defined

module licese-> 

the kernel 

```Makefile
obj-m += test_mod00.o

KDIR=/usr/src/linux-headers-5.19.0-41-generic

  

CFLAGS = -D_KERNEL_ -DMODULE -I$(KDIR)/include -Wall

  

all:

$(MAKE) -C $(KDIR) M=$(shell pwd) $(KCONFIG) modules

clean:

$(MAKE) -C $(KDIR) M=$(shell pwd) clean

rm -f *.o
```

# 04272023


Everything that you build so far is in the USER SPACE
![[Pasted image 20230427173242.png]]
the standard library (malloc, printf, mat function, only available in user space, not in kernel space)

CROSS COMPILE:
"Build application for differen machine etc"
![[Pasted image 20230427173425.png]]
you compile successfuly, you will have extension .ko
insert this module by hand
want to test our kernel modules

first one to initialize (to reserve resources like memory or interrupt)
make sure you realease all of those resources
kernel module does not have a main function or a start function, this will run in a kernel memory space

pay attention to this structure called
# FILE OPERATION

file operation is just a structure of mostly a function pointer
there is another tool called make, that will compile your source code accordingly

kernel does not care about our shell
dmesg will print all of the log file
filter the output from the log
filters the log :
## GREP

pay attention to line no 3
"Path to the source file that will use to compile your kernel"
the most important resource is your man pages
man pages for kernel
 ![[Pasted image 20230427174553.png]]
how can you figure out what your real number

uname -a
![[Pasted image 20230427174637.png]]
the more variables we have in the make file, the more compilcated it becomes
printscreen with the make file and improve the make file
list of instruction here

![[Pasted image 20230427174739.png]]
replace your gcc, make will call your compiler

lsmod will list your module, similar with PS or task manager in windows
feature of adding modules to it (like those extensions that you put in your browser (like adblock plus) "I want to improve the kernel and add functionalities")
"extensions to your kernel" 
embedded system, you usually strip down the kernel into bare minimum 

grep test will fiter the lsmod and filter anything with test in the name
"removes the line that have string" -v (only removes the lines that contains that)

red line
sudo insmod test_mod00.ko
this will install your "extension", in our case it will load the module

the first time you run those instruction, it will not find the one that name test
after the first one, you will find the module in the list
in either case if its work or not work, you can run the next instruction

dmesg -> will print all the messages from your kernel space
from your kernel workspace
if insert module is successful, at the end of the log file there'll be your log message
tail-> will keep the tail of that file / list or log lines
if your insert module failed, you will see the line at the end that explain why it failed

tainted kernel module
version that you use to compile the module is not the same 
you need to change your make file
or you need to change the name -> use uname instead of building that path by yourself

lsmod will tell you if you have new module with name test
inside this hello world module, you can see the clear message as well

![[Pasted image 20230427180124.png]]
![[Pasted image 20230427180139.png]]

Should transfer some data from user space to kernel space
file operation
on file system -> our driver at some point will look like a file
and the way you read and write to your driver is by using the standard c function for reading and writing inside files

userspace application that will use the fopen, fread, fwrite
we dont know how is it linked yet

we introduce this new function
4k-> common size for a page 
our buffer

can get the address of that ten elements (10 11 12 and so on)
in this case tis offset is 0
will start from the beginning
this copy from user
will try at least to copy this much data

copy from user and move it to the kernel space 

![[Pasted image 20230427181205.png]]
implement a function that suppose to do a read
let's see what we have to do here:
2 pointer, one for write and one for read, and we move it independently

![[Pasted image 20230427181507.png]]

register character device
there're a newer implmenetations
we use old version because we want to do it by ourself
we want to see where we create it inside our file system
for your sample, can find the newer version of this 

to add one more
iocontrol (iocpo)

once it starting executed, then this module is already in kernel
it might failed to allocate resources
but if you remove the module, you need to know which one you want to steal

system might not have available interrupt for you

![[Pasted image 20230427182303.png]]

![[Pasted image 20230427182315.png]]

major number, assigned to your driver

create an access point to our driver, with a form of a file
your module can be loaded 2ice

list of character in the front
c -> character device
d -> directory or folder
or nothing
permission file for the owner of this file, in this case is he root
usually: read, write, and execute (r, w, x)

sudo chmod 0777 -> in c and this terminal that 0 is used to octal value
0x -> hexadecimal value
0 -> octal value
octal use 3 bits
hexa use 4 bits




![[Pasted image 20230427183507.png]]
redirect symbol
echo
get placed on default on the output

in c you need to end your string with a  backslash 0


last seminar is not a group anymore
2 week to the end of the semester
to show that they can build and run a module
customize this module a little bit
iocontrol -> figure that out by yourself
fileops -> add new pointer iocto -> and map it to your function
to reset the pointer to the beginning
explain what kind of meaning your driver has

20 different words
will pick different words from there
:wordle game

![[Pasted image 20230502175439.png]]

read pointer, the other value of where you want to set the read pointer
set read pointer to 0s

![[Pasted image 20230502175542.png]]



![[Pasted image 20230502181214.png]]

NOTES:
```
sudo sysctl kernel.dmesg_restrict=0
```

Two user space application
link fopen,
fgets, fclose

read few characters and print it out

load test mod 01, 5 points for that
add user space, get 2 more points(don't change the kernel space)

file called source.c
inside that file you have include stdio.h
int main etc
return 0

this is where you need to use fopen, 
fgets
fclose
string
print

if you do a gcc source.c, it will create a.out
a.out here is that guy
fopen something they need to be inside the source file 
doesnt have anything to do with the kernel space
that file will think that this is the text file

refers to the module as a text file
you can fopen it and it will read as a test file


someone will use the fops part
looks like maybe you hack my device
but i use fake function, so you think that you register properly
