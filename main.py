import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper


@execution_time
def algorithm(teamA: list, teamB: list) -> list:
    teamA.sort()
    result = []
    for playB in teamB:
        counter = 0
        for playA in teamA:
            if playA > playB:
                break
            counter += 1
        result.append(counter)
    return result


@execution_time
def faster(teamA: list, teamB: list) -> list:
    teamA.sort()
    result = []
    for index, playB in enumerate(teamB):
        if index == 0 or teamB[index - 1] > playB:
            counter = 0
        while counter < len(teamA) and teamA[counter] <= playB:
            counter += 1
        result.append(counter)
    return result


def main():
    algorithm([x*2 for x in range(1000000)], [x for x in range(1000, 2)])
    faster([x*2 for x in range(1000000)], [x for x in range(1000, 2)])
    assert faster([1, 2, 5, 3, 6, 8], [8, 0, 10, 4]) == [6, 0, 6, 3]
    assert faster([0], [8, 0, 10, 4]) == [1, 1, 1, 1]
    assert faster([90, 0, 1], [0]) == [1]
    assert faster([0], [0]) == [1]
    assert faster([100, 200, 6, 9 ], [4, 2, 1, 0, 0, 2]) == [0, 0, 0, 0, 0, 0]
    assert algorithm([1, 2, 5, 3, 6, 8], [8, 0, 10, 4]) == [6, 0, 6, 3]
    assert algorithm([0], [8, 0, 10, 4]) == [1, 1, 1, 1]
    assert algorithm([90, 0, 1], [0]) == [1]
    assert algorithm([0], [0]) == [1]
    assert algorithm([100, 200, 6, 9 ], [4, 2, 1, 0, 0, 2]) == [0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    main()
