# include <linux/unistd.h>
# include <sys/syscall.h>

int main() {
        syscall(333);
        return 0;
}
