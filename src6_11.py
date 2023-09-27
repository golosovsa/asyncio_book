"""
Параллельное инкриминирование разделяемого счетчика
(может привести к ошибке, порождает состояние гонки)
с. 177
"""
from multiprocessing import Process, Value, Array


def increment_value(shared_int: Value):
    shared_int.value += 1


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
