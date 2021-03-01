also known as [[intraprocess communication]]

mutex: A single variable that can be locked or unlocked, uses the hardware instruction "test and set" which entirely locks the [[RAM]] from *all the cores*

semaphore: if count is negative *n*, *n* threads are blocked on the semaphore, allows you to count how many threads are waiting.

barriers: wait until that many threads hit the barrier (implemented with semaphores)

[[model checking]]

early days of Linux the kernel only had one lock which lead to a lot of slowness

fairness: threads don't sleep for too long
progress: threads don't sleep forever

kill sends to any thread in that process. pthread sends to the specific thread, and pthread_cond_signal sends to anyone blocking

