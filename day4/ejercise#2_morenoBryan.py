import itertools
def nearest_leg_lengths(coin_thicknesses, table_heights):
    def possible_leg_lengths(coin_thicknesses, target_height):
        min_leg_length = max(coin_thicknesses)
        max_leg_length = sum(coin_thicknesses)
        possible_lengths = []
        for i in range(1, len(coin_thicknesses) + 1):
            for combination in itertools.combinations(coin_thicknesses, i):
                total_thickness = sum(combination)
                if min_leg_length <= total_thickness <= target_height:
                    possible_lengths.append(total_thickness)
        return min(possible_lengths), max(possible_lengths)

    results = []
    for table_height in table_heights:
        min_leg_length, max_leg_length = possible_leg_lengths(coin_thicknesses, table_height)
        results.append((min_leg_length, max_leg_length))
    return results

def read_input():
    while True:
        n, t = map(int, input().split())
        if n == 0 and t == 0:
            break
        coin_thicknesses = [int(x) for x in input().split()]
        table_heights = [int(x) for x in input().split()]
        yield coin_thicknesses, table_heights

for coin_thicknesses, table_heights in read_input():
    results = nearest_leg_lengths(coin_thicknesses, table_heights)
    for min_leg_length, max_leg_length in results:
        print(min_leg_length, max_leg_length)