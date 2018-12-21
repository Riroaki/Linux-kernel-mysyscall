# Start to build the kernel.
make
make modules
make modules_install
make install
reboot
