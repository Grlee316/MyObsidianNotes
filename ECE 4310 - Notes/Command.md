make

lsmod | grep test

sudo insmod test_mod03.ko

lsmod | grep test

sudo dmesg | tail

cat /proc/devices | grep test

sudo mknod /dev/test_mod03 c 509 1

ll /dev/ | grep test (to see permission)

sudo chmod 0777 /dev/test_mod03 


chmod -> change mode
mknod -> create a special file or device file in the file system

How to move files:
https://opensource.com/article/19/8/moving-files-linux-depth

