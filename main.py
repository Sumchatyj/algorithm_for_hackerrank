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


def main():
    assert algorithm([1, 2, 5, 3, 6, 8], [8, 0, 10, 4]) == [6, 0, 6, 3]
    assert algorithm([0], [8, 0, 10, 4]) == [1, 1, 1, 1]
    assert algorithm([90, 0, 1], [0]) == [1]
    assert algorithm([0], [0]) == [1]
    assert algorithm([100, 200, 6, 9 ], [4, 2, 1, 0, 0, 2]) == [0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    main()
