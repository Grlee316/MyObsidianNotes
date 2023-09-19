The operating system segregates virtual memory into kernel space and userspace.  Kernel space is strictly reserved for running the kernel, kernel extensions, and most device drivers. In contrast, user space is the memory area where all user-mode applications work, and this memory can be swapped out when necessary. 

There are many ways to Communicate between the Userspace and Kernel Space, they are:

-   **IOCTL**
-   [Procfs](https://embetronicx.com/tutorials/linux/device-drivers/procfs-in-linux/)
-   [Sysfs](https://embetronicx.com/tutorials/linux/device-drivers/sysfs-in-linux-kernel/)
-   Configfs
-   Debugfs
-   Sysctl
-   UDP Sockets
-   Netlink Sockets

In this tutorial, we will see IOCTL.

## IOCTL in Linux

## IOCTL

[IOCTL](https://en.wikipedia.org/wiki/Ioctl) is referred to as Input and Output Control, which is used to talk to device drivers. This system call is available in most driver categories.  The major use of this is in case of handling some specific operations of a device for which the kernel does not have a system call by default.

Some real-time applications of ioctl are Ejecting the media from a “cd” drive, changing the Baud Rate of Serial port, Adjusting the Volume, Reading or Writing device registers, etc. We already have the write and read function in our device driver. But it is not enough for all cases.

## Steps involved in IOCTL

There are some steps involved to use IOCTL.

-   Create IOCTL command in the driver
-   Write IOCTL function in the driver
-   Create IOCTL command in a Userspace application
-   Use the IOCTL system call in a Userspace

### Create IOCTL Command in the Driver

To implement a new ioctl command we need to follow the following steps.

1. Define the ioctl command

**`#define "ioctl name" __IOX("magic number","command number","argument type")`**

where _**`IOX`**_ can be :  
“**`IO`**“: an ioctl with no parameters  
“**`IOW`**“: an ioctl with write parameters (copy_from_user)  
“**`IOR`**“: an ioctl with read parameters (copy_to_user)  
“**`IOWR`**“: an ioctl with both write and read parameters

-   The **`Magic Number`** is a unique number or character that will differentiate our set of ioctl calls from the other ioctl calls. some times the major number for the device is used here.
-   Command Number is the number that is assigned to the ioctl. This is used to differentiate the commands from one another.
-   The last is the type of data.

2. Add the header file **`linux/ioctl.h`** to make use of the above-mentioned calls.

#### **Example**
```
#include <linux/ioctl.h>
#define WR_VALUE _IOW('a','a',int32_t*)
#define RD_VALUE _IOR('a','b',int32_t*)
```

### Write IOCTL function in the driver

The next step is to implement the ioctl call we defined into the corresponding driver. We need to add the ioctl function to our driver. Find the prototype of the function below.

**`int  ioctl(struct inode *inode,struct file *file,unsigned int cmd,unsigned long arg)`**

Where

<**`inode`**>: is the inode number of the file being worked on.  
<**`file`**>: is the file pointer to the file that was passed by the application.  
<**`cmd`**>: is the ioctl command that was called from the userspace.  
<**`arg`**>: are the arguments passed from the userspace

Within the function “ioctl” we need to implement all the commands that we defined above (**`WR_VALUE`**, **`RD_VALUE`**). We need to use the same commands in the **`switch`** statement which is defined above.

Then we need to inform the kernel that the ioctl calls are implemented in the function “**`etx_ioctl`**“. This is done by making the **`fops`** pointer “**`unlocked_ioctl`**” to point to “**`etx_ioctl`**” as shown below.

```c
/*
** This function will be called when we write IOCTL on the Device file
*/
static long etx_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
         switch(cmd) {
                case WR_VALUE:
                        if( copy_from_user(&value ,(int32_t*) arg, sizeof(value)) )
                        {
                                pr_err("Data Write : Err!\n");
                        }
                        pr_info("Value = %d\n", value);
                        break;
                case RD_VALUE:
                        if( copy_to_user((int32_t*) arg, &value, sizeof(value)) )
                        {
                                pr_err("Data Read : Err!\n");
                        }
                        break;
                default:
                        pr_info("Default\n");
                        break;
        }
        return 0;
}

/*
** File operation sturcture
*/
static struct file_operations fops =
{
        .owner          = THIS_MODULE,
        .read           = etx_read,
        .write          = etx_write,
        .open           = etx_open,
        .unlocked_ioctl = etx_ioctl,
        .release        = etx_release,
};
```

Now we need to call the ioctl command from a user application.

### Create IOCTL command in a Userspace application

Just define the ioctl command like how we defined it in the driver.

**Example:**

```
#define WR_VALUE _IOW('a','a',int32_t*)
#define RD_VALUE _IOR('a','b',int32_t*)
```

### Use IOCTL system call in Userspace

Include the header file **`<sys/ioctl.h>`**.Now we need to call the new ioctl command from a user application.

**`long ioctl( "file descriptor","ioctl command","Arguments");`**

Where,

<**`file descriptor`**>: This the open file on which the ioctl command needs to be executed, which would generally be device files.  
<**`ioctl command`**>: ioctl command which is implemented to achieve the desired functionality  
<**`arguments`**>: The arguments need to be passed to the ioctl command.

#### **Example**
```c
ioctl(fd, WR_VALUE, (int32_t*) &number); 
ioctl(fd, RD_VALUE, (int32_t*) &value);
```

Now we will see the complete driver and application.

## IOCTL in Linux – Device Driver Source Code

In this example we only implemented IOCTL. In this driver, I’ve defined one variable (**`int32_t value`**). Using ioctl command we can read or change the variable. So other functions like open, close, read, and write, We simply left empty. Just go through the code below.

**driver.c**
```c
/***************************************************************************//**
*  \file       driver.c
*
*  \details    Simple Linux device driver (IOCTL)
*
*  \author     EmbeTronicX
*
*  \Tested with Linux raspberrypi 5.10.27-v7l-embetronicx-custom+
*
*******************************************************************************/
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kdev_t.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include<linux/slab.h>                 //kmalloc()
#include<linux/uaccess.h>              //copy_to/from_user()
#include <linux/ioctl.h>
#include <linux/err.h>
 
 
#define WR_VALUE _IOW('a','a',int32_t*)
#define RD_VALUE _IOR('a','b',int32_t*)
 
int32_t value = 0;
 
dev_t dev = 0;
static struct class *dev_class;
static struct cdev etx_cdev;

/*
** Function Prototypes
*/
static int      __init etx_driver_init(void);
static void     __exit etx_driver_exit(void);
static int      etx_open(struct inode *inode, struct file *file);
static int      etx_release(struct inode *inode, struct file *file);
static ssize_t  etx_read(struct file *filp, char __user *buf, size_t len,loff_t * off);
static ssize_t  etx_write(struct file *filp, const char *buf, size_t len, loff_t * off);
static long     etx_ioctl(struct file *file, unsigned int cmd, unsigned long arg);

/*
** File operation sturcture
*/
static struct file_operations fops =
{
        .owner          = THIS_MODULE,
        .read           = etx_read,
        .write          = etx_write,
        .open           = etx_open,
        .unlocked_ioctl = etx_ioctl,
        .release        = etx_release,
};

/*
** This function will be called when we open the Device file
*/
static int etx_open(struct inode *inode, struct file *file)
{
        pr_info("Device File Opened...!!!\n");
        return 0;
}

/*
** This function will be called when we close the Device file
*/
static int etx_release(struct inode *inode, struct file *file)
{
        pr_info("Device File Closed...!!!\n");
        return 0;
}

/*
** This function will be called when we read the Device file
*/
static ssize_t etx_read(struct file *filp, char __user *buf, size_t len, loff_t *off)
{
        pr_info("Read Function\n");
        return 0;
}

/*
** This function will be called when we write the Device file
*/
static ssize_t etx_write(struct file *filp, const char __user *buf, size_t len, loff_t *off)
{
        pr_info("Write function\n");
        return len;
}

/*
** This function will be called when we write IOCTL on the Device file
*/
static long etx_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
         switch(cmd) {
                case WR_VALUE:
                        if( copy_from_user(&value ,(int32_t*) arg, sizeof(value)) )
                        {
                                pr_err("Data Write : Err!\n");
                        }
                        pr_info("Value = %d\n", value);
                        break;
                case RD_VALUE:
                        if( copy_to_user((int32_t*) arg, &value, sizeof(value)) )
                        {
                                pr_err("Data Read : Err!\n");
                        }
                        break;
                default:
                        pr_info("Default\n");
                        break;
        }
        return 0;
}
 
/*
** Module Init function
*/
static int __init etx_driver_init(void)
{
        /*Allocating Major number*/
        if((alloc_chrdev_region(&dev, 0, 1, "etx_Dev")) <0){
                pr_err("Cannot allocate major number\n");
                return -1;
        }
        pr_info("Major = %d Minor = %d \n",MAJOR(dev), MINOR(dev));
 
        /*Creating cdev structure*/
        cdev_init(&etx_cdev,&fops);
 
        /*Adding character device to the system*/
        if((cdev_add(&etx_cdev,dev,1)) < 0){
            pr_err("Cannot add the device to the system\n");
            goto r_class;
        }
 
        /*Creating struct class*/
        if(IS_ERR(dev_class = class_create(THIS_MODULE,"etx_class"))){
            pr_err("Cannot create the struct class\n");
            goto r_class;
        }
 
        /*Creating device*/
        if(IS_ERR(device_create(dev_class,NULL,dev,NULL,"etx_device"))){
            pr_err("Cannot create the Device 1\n");
            goto r_device;
        }
        pr_info("Device Driver Insert...Done!!!\n");
        return 0;
 
r_device:
        class_destroy(dev_class);
r_class:
        unregister_chrdev_region(dev,1);
        return -1;
}

/*
** Module exit function
*/
static void __exit etx_driver_exit(void)
{
        device_destroy(dev_class,dev);
        class_destroy(dev_class);
        cdev_del(&etx_cdev);
        unregister_chrdev_region(dev, 1);
        pr_info("Device Driver Remove...Done!!!\n");
}
 
module_init(etx_driver_init);
module_exit(etx_driver_exit);
 
MODULE_LICENSE("GPL");
MODULE_AUTHOR("EmbeTronicX <embetronicx@gmail.com>");
MODULE_DESCRIPTION("Simple Linux device driver (IOCTL)");
MODULE_VERSION("1.5");
```

**Makefile:**
```Makefile
obj-m += driver.o
 
KDIR = /lib/modules/$(shell uname -r)/build
 
 
all:
  make -C $(KDIR)  M=$(shell pwd) modules
 
clean:
  make -C $(KDIR)  M=$(shell pwd) clean
```



## IOCTL in Linux – Application Source Code

This application is used to write the value to the driver. Then read the value again.

**test_app.c**
```c
/***************************************************************************//**
*  \file       test_app.c
*
*  \details    Userspace application to test the Device driver
*
*  \author     EmbeTronicX
*
*  \Tested with Linux raspberrypi 5.10.27-v7l-embetronicx-custom+
*
*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include<sys/ioctl.h>
 
#define WR_VALUE _IOW('a','a',int32_t*)
#define RD_VALUE _IOR('a','b',int32_t*)
 
int main()
{
        int fd;
        int32_t value, number;
        printf("*********************************\n");
        printf("*******WWW.EmbeTronicX.com*******\n");
 
        printf("\nOpening Driver\n");
        fd = open("/dev/etx_device", O_RDWR);
        if(fd < 0) {
                printf("Cannot open device file...\n");
                return 0;
        }
 
        printf("Enter the Value to send\n");
        scanf("%d",&number);
        printf("Writing Value to Driver\n");
        ioctl(fd, WR_VALUE, (int32_t*) &number); 
 
        printf("Reading Value from Driver\n");
        ioctl(fd, RD_VALUE, (int32_t*) &value);
        printf("Value is %d\n", value);
 
        printf("Closing Driver\n");
        close(fd);
}
```

## Building Driver and Application

-   Build the driver by using Makefile (**`sudo make`**)
-   Use the below line in the terminal to compile the user space application.

gcc -o test_app test_app.c

![[Pasted image 20230509180747.png]]

This is a simple example of using ioctl in a Linux device driver. If you want to send multiple arguments, put those variables into the structure, and pass the address of the structure.

In our [next tutorial](https://embetronicx.com/tutorials/linux/device-drivers/procfs-in-linux/), we will see another userspace and kernel space communication method which is **`procfs`**.

Please find the other Linux device driver tutorials [here](https://embetronicx.com/linux-device-driver-tutorials/).

You can also read the below tutorials.
