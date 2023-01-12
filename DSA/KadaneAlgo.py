from sys import maxsize
def kadane(arr):
    max_sofar = -maxsize
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < -maxsize:
            max_ending_here = -maxsize
        if max_ending_here > max_sofar:
            max_sofar  = max_ending_here
    return max_sofar
