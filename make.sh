# Start to build the kernel.
cd linux-4.8/
make
make modules
make modules_install
make install
reboot
