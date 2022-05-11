"""Filtering Data Based on Criteria"""
# by creating a mask function

col_data: dict[str, list[float]] = {
    'high': [77, 84, 78, 79, 65, 67, 74, 61, 55, 61],
    'low': [67, 51, 64, 45, 43, 53, 56, 37, 34, 42],
    'rain': [.3, .2, .4, .8, 0., .2, .4, .5, .1, .1]
}


# Produce a mask based on criteria
def less_than(col: list[float], threshold: float) -> list[bool]:
    result: list[bool] = []
    for item in col:
        result.append(item < threshold)
    return result


# Takes in a column and a list of masks (bool values), returns only th values in the input column
# where the corresponding mask value is True.
def masked(col: list[float], mask: list[bool]) -> list[float]:
    result: list[float] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


def mean(col: list[float]) -> float:
    return sum(col) / len(col)


def main():
    no_rain_mask: list[bool] = less_than(col_data['rain'], 0.3)
    print(no_rain_mask)
    result: list[float] = masked(col_data['high'], no_rain_mask)
    print(result)
    avg: float = mean(result)
    print(avg)
    # code can now be easily be re-used for other analysis
    cold_day_mask: list[bool] = less_than(col_data['low'], 50)
    print(cold_day_mask)
    result: list[float] = masked(col_data['rain'], cold_day_mask)
    print(result)
    avg: float = mean(result)
    print(avg)


if __name__ == '__main__':
    main()
