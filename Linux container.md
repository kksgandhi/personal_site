containers are on top of the Linux kernel, but do not require their own kernel. Each process within a container has a local pid and a global pid.

programs and non-kernel things are installed into the container. Syscalls fall through into the real kernel
