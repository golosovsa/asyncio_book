"""
Захват и освобождение блокировки
с. 180
"""
from multiprocessing import Process, Value, Array


def increment_value(shared_int: Value):
    with shared_int.get_lock():
        shared_int.value += 1
    # shared_int.get_lock().acquire()
    # shared_int.value += 1
    # shared_int.get_lock().release()


if __name__ == '__main__':
    integer = Value('i', 0)
    integer_array = Array('i', [0, 0])
    procs = [
        Process(target=increment_value, args=(integer, )),
        Process(target=increment_value, args=(integer,)),
    ]
    [p.start() for p in procs]
    [p.join() for p in procs]

    print(integer.value)
    assert integer.value == 2
