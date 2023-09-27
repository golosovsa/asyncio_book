"""
Распараллеливание с помощью MapReduce и пула процессов
"""
import asyncio
import concurrent.futures
import functools
import time


def partition(data: list, chunk_size: int) -> list:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: list[str]) -> dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] += int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] += second[key]
        else:
            merged[key] = second[key]
    return merged


async def main(partition_size: int):
    with open('googlebooks-eng-all-1gram-20120701-a', 'rt', encoding='utf-8') as f:
        contents = f.readlines()
    loop = asyncio.get_running_loop()
    tasks = []
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        for chunk in partition(contents, partition_size):
            tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

        intermediate_results = await asyncio.gather(*tasks)
        final_result = functools.reduce(merge_dictionaries, intermediate_results)

        print(f'Aardvark встречается {final_result["Aardvark"]} раз.')
        end = time.time()
        print(f'Время MapReduce: {(end-start):.4f} секунд')


if __name__ == '__main__':
    asyncio.run(main(partition_size=60000))
