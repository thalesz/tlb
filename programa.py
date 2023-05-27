import sys
import time
import ctypes

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <number_of_pages> <number_of_iterations>")
        return

    num_pages = int(sys.argv[1])
    num_iterations = int(sys.argv[2])

    page_size = ctypes.CDLL("libc.so.6").sysconf(ctypes.c_int(30))  # 30 corresponds to _SC_PAGESIZE
    elements_per_page = page_size // sys.getsizeof(int)
    vector_size = num_pages * elements_per_page
    vector = [0] * vector_size

    stride = elements_per_page

    total_time = 0

    for j in range(num_iterations):
        start_time = time.time()

        for i in range(0, num_pages * stride, stride):
            vector[i] += 1

        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / (num_pages * num_iterations) * 1e6  # Convert to microseconds

    print("Average time per access: {:.2f} microseconds".format(average_time))

if __name__ == "__main__":
    main()
import sys
import time
import ctypes

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <number_of_pages> <number_of_iterations>")
        return

    num_pages = int(sys.argv[1])
    num_iterations = int(sys.argv[2])

    page_size = ctypes.CDLL("libc.so.6").sysconf(ctypes.c_int(30))  # 30 corresponds to _SC_PAGESIZE
    elements_per_page = page_size // sys.getsizeof(int)
    vector_size = num_pages * elements_per_page
    vector = [0] * vector_size

    stride = elements_per_page

    total_time = 0

    for j in range(num_iterations):
        start_time = time.time()

        for i in range(0, num_pages * stride, stride):
            vector[i] += 1

        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / (num_pages * num_iterations) * 1e6  # Convert to microseconds

    print("Average time per access: {:.2f} microseconds".format(average_time))

if __name__ == "__main__":
    main()
