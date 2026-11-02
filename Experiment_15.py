import gc
import tracemalloc


def create_cycles(count):
    cycles = []
    for _ in range(count):
        cycle = []
        cycle.append(cycle)
        cycles.append(cycle)
    return cycles


def display_memory(message):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{message}: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")


def main():
    tracemalloc.start()
    gc.disable()

    display_memory("Memory before creating cycles")

    cycles = create_cycles(1000)
    del cycles
    display_memory("Memory after creating cycles")

    collected = gc.collect()
    print(f"Garbage collector collected {collected} objects.")
    display_memory("Memory after garbage collection")

    gc.enable()
    tracemalloc.stop()


if __name__ == "__main__":
    main()
