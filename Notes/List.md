
make

lsmod | grep test

sudo insmod test_mod02.ko

lsmod | grep test

sudo dmesg | tail

cat /proc/devices | grep test

sudo mknod /dev/test_mod02 c 509 1  (make node)

ll /dev/ | grep test (to see the permision)

sudo chmod 0777 /dev/test_mod02 (this is to change the read and write permission)


To REMOVE:
sudo rmmod test_mod02
lsmod | grep test (to check)
sudo dmesg|tail